import base64
import json
import time
import webbrowser

from datetime import datetime
from http.server import HTTPServer
from pathlib import Path
from threading import Thread
from typing import Dict

import jwt
import requests

from bargaineer.schwab import OAUTH_TOKEN_URL


def __token__(client_id: str, client_secret: str, token: Path, data: Dict[str, str]):
    response = requests.post(
        OAUTH_TOKEN_URL,
        headers={
            "Authorization": f"Basic {base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()}",
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data=data,
    )

    if response.status_code == 200:
        with token.open("w") as f:
            json.dump(response.json(), f)


def login(server: HTTPServer, redirect_uri: str, token: Path):
    t = Thread(target=server.serve_forever)
    t.start()

    webbrowser.open(redirect_uri)
    while not token.exists():
        time.sleep(1)

    server.shutdown()
    t.join()


def authorize(
    client_id: str, client_secret: str, redirect_uri: str, token: Path, code: str
):
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }
    __token__(client_id, client_secret, token, data)


def refresh(client_id: str, client_secret: str, token: Path):
    with token.open("r") as f:
        tokens = json.load(f)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": tokens["refresh_token"],
        }
        __token__(client_id, client_secret, token, data)


def is_expired(token: Path) -> Dict[str, bool]:
    EXPIRATION_TIMES = {"access": 1800, "refresh": 604800}
    with token.open("r") as f:
        tokens = json.load(f)
        payload = jwt.decode(
            tokens["id_token"],
            algorithms=["HS256"],
            options={"verify_signature": False},
        )
        return {
            key: datetime.now().timestamp() >= (payload["iat"] + value)
            for key, value in EXPIRATION_TIMES.items()
        }
