from requests import Response

from .. import client
from . import TRADER_URL


def get() -> Response:
    return client.request(f"{TRADER_URL}/userPreference")
