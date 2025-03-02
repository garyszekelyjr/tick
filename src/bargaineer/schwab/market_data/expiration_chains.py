from requests import Response

from .. import client
from . import MARKET_DATA_URL


def get(symbol: str) -> Response:
    url = f"{MARKET_DATA_URL}/expirationchain"
    params = {"symbol": symbol}
    return client.request(url, params=params)
