import base64
import time
import webbrowser

from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from typing import Dict
from urllib.parse import parse_qs, urlencode, urlparse

import requests

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import ENGINE, models

from . import (
    CLIENT_ID,
    CLIENT_SECRET,
    CONTEXT,
    OAUTH_AUTHORIZE_URL,
    OAUTH_TOKEN_URL,
    REDIRECT_URI,
)


def __token__(data: Dict[str, str]):
    response = requests.post(
        OAUTH_TOKEN_URL,
        headers={
            "Authorization": f"Basic {base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=data,
    )

    if response.status_code == 200:
        with Session(ENGINE) as session:
            token = models.Token(
                **response.json(),
                access_token_expires=datetime.now().timestamp() + 1800,
                refresh_token_expires=datetime.now().timestamp() + 604800,
            )
            session.add(token)
            session.commit()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)
        code = params.get("code", None)

        if code:
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": REDIRECT_URI,
            }
            __token__(data)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
        else:
            params = {
                "client_id": CLIENT_ID,
                "redirect_uri": REDIRECT_URI,
            }
            self.send_response(302)
            self.send_header("Location", f"{OAUTH_AUTHORIZE_URL}?{urlencode(params)}")
            self.end_headers()


def authorize():
    server = HTTPServer(("127.0.0.1", 443), Handler)
    server.socket = CONTEXT.wrap_socket(server.socket, server_side=True)

    t = Thread(target=server.serve_forever)
    t.start()

    webbrowser.open(REDIRECT_URI)
    with Session(ENGINE) as session:
        while not session.scalar(select(models.Token)):
            time.sleep(1)

        server.shutdown()
        t.join()
        return session.scalar(select(models.Token))


def refresh():
    with Session(ENGINE) as session:
        token = session.scalar(select(models.Token))
        assert token
        data = {
            "grant_type": "refresh_token",
            "refresh_token": token.refresh_token,
        }
        session.delete(token)
        session.commit()
        __token__(data)
        return session.scalar(select(models.Token))
