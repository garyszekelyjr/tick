from requests import Response

from .. import client
from . import TRADER_URL


def account_numbers() -> Response:
    return client.request(f"{TRADER_URL}/accounts/accountNumbers")


def get_all() -> Response:
    return client.request(f"{TRADER_URL}/accounts")


def get(account_number: str) -> Response:
    return client.request(f"{TRADER_URL}/accounts/{account_number}")
