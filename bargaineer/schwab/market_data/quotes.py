from enum import Enum
from typing import List

from requests import Response

from .. import client
from . import MARKET_DATA_URL


class Field(Enum):
    QUOTE = "quote"
    FUNDAMENTAL = "fundamental"
    EXTENDED = "extended"
    REFERENCE = "reference"
    REGULAR = "regular"


def quotes(
    symbols: List[str],
    fields: List[Field] = [field for field in Field],
    indicative: bool = False,
) -> Response:
    url = f"{MARKET_DATA_URL}/quotes"
    params = {
        "symbols": ",".join(symbols),
        "fields": ",".join([field.value for field in fields]),
        "indicative": str(indicative).lower(),
    }
    return client.request(url, params=params)


def quote(
    symbol: str,
    fields: List[Field] = [field for field in Field],
) -> Response:
    url = f"{MARKET_DATA_URL}/{symbol}/quotes"
    params = {"fields": ",".join([field.value for field in fields])}
    return client.request(url, params=params)
