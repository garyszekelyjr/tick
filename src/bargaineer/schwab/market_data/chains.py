from enum import Enum

from requests import Response

from .. import client
from . import MARKET_DATA_URL


class ContractType(Enum):
    CALL = "CALL"
    PUT = "PUT"
    ALL = "ALL"


def get(
    symbol: str,
    contract_type: ContractType = ContractType.ALL,
    strike_count: int | None = None,
) -> Response:
    url = f"{MARKET_DATA_URL}/chains"
    params = {"symbol": symbol, "contractType": contract_type.value}
    if strike_count:
        params["strikeCount"] = str(strike_count)
    return client.request(url, params=params)
