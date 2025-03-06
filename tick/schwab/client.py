from datetime import datetime
from typing import Dict

import requests

from sqlalchemy import select
from sqlalchemy.orm import Session

from .. import ENGINE, models
from . import utilities


def request(
    url: str,
    method: str = "GET",
    params: Dict[str, str] | None = None,
    data: Dict[str, str] | None = None,
):
    with Session(ENGINE) as session:
        token = session.scalar(select(models.Token))

        if not token:
            print("Tokens Not Found. Authenticating...")
            token = utilities.authorize()

        assert token

        if datetime.now().timestamp() >= token.refresh_token_expires:
            print("Refresh Token Expired. Reauthenticating...")
            token = utilities.authorize()

        assert token

        if datetime.now().timestamp() >= token.access_token_expires:
            print("Access Token Expired. Refreshing...")
            token = utilities.refresh()

        assert token

        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {token.access_token}",
        }

        return requests.request(method, url, params=params, data=data, headers=headers)
