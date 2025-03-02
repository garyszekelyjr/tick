import json
import ssl

from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict
from urllib.parse import parse_qs, urlencode, urlparse

import requests

from .. import SECRETS
from . import (
    CLIENT_ID,
    CLIENT_SECRET,
    OAUTH_AUTHORIZE_URL,
    PEM_PASSWORD,
    REDIRECT_URI,
    TOKEN,
)

from . import utilities


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)
        code = params.get("code", None)

        if code:
            authorized = utilities.authorize(
                CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN, code.pop()
            )
            self.send_response(200 if authorized else 401)
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


SERVER = HTTPServer(("127.0.0.1", 443), Handler)
CONTEXT = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
CONTEXT.load_cert_chain(SECRETS / "cert.pem", SECRETS / "key.pem", PEM_PASSWORD)
SERVER.socket = CONTEXT.wrap_socket(SERVER.socket, server_side=True)


def request(
    url: str,
    method: str = "GET",
    params: Dict[str, str] | None = None,
    data: Dict[str, str] | None = None,
):
    if not TOKEN.exists():
        print("Tokens Not Found. Authenticating...")
        utilities.login(SERVER, REDIRECT_URI, TOKEN)

    is_expired = utilities.is_expired(TOKEN)

    if is_expired["refresh"]:
        print("Refresh Token Expired. Reauthenticating...")
        utilities.login(SERVER, REDIRECT_URI, TOKEN)

    if is_expired["access"]:
        print("Access Token Expired. Refreshing...")
        utilities.refresh(CLIENT_ID, CLIENT_SECRET, TOKEN)

    with TOKEN.open("r") as f:
        tokens = json.load(f)

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {tokens["access_token"]}",
        }

        return requests.request(method, url, params=params, data=data, headers=headers)
