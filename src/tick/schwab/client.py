import json

from typing import Dict

import requests

from . import (
    TOKEN,
    utilities,
)


def request(
    url: str,
    method: str = "GET",
    params: Dict[str, str] | None = None,
    data: Dict[str, str] | None = None,
):
    if not TOKEN.exists():
        print("Tokens Not Found. Authenticating...")
        utilities.authorize()

    expired = utilities.is_expired()

    if expired["refresh"]:
        print("Refresh Token Expired. Reauthenticating...")
        utilities.authorize()

    if expired["access"]:
        print("Access Token Expired. Refreshing...")
        utilities.refresh()

    with TOKEN.open("r") as f:
        tokens = json.load(f)

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {tokens["access_token"]}",
        }

        return requests.request(method, url, params=params, data=data, headers=headers)
