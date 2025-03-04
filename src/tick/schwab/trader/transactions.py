from datetime import datetime
from enum import Enum

from requests import Response

from .. import client
from . import TRADER_URL


class Types(Enum):
    TRADE = "TRADE"
    RECEIVE_AND_DELIVER = "RECEIVE_AND_DELIVER"
    DIVIDEND_OR_INTEREST = "DIVIDEND_OR_INTEREST"
    ACH_RECEIPT = "ACH_RECEIPT"
    ACH_DISBURSEMENT = "ACH_DISBURSEMENT"
    CASH_RECEIPT = "CASH_RECEIPT"
    CASH_DISBURSEMENT = "CASH_DISBURSEMENT"
    ELECTRONIC_FUND = "ELECTRONIC_FUND"
    WIRE_OUT = "WIRE_OUT"
    WIRE_IN = "WIRE_IN"
    JOURNAL = "JOURNAL"
    MEMORANDUM = "MEMORANDUM"
    MARGIN_CALL = "MARGIN_CALL"
    MONEY_MARKET = "MONEY_MARKET"
    SMA_ADJUSTMENT = "SMA_ADJUSTMENT"


def get_all(
    account_number: str,
    start_date: datetime,
    end_date: datetime,
    symbol: str = "",
    types: str = "",
) -> Response:
    url = f"{TRADER_URL}/accounts/{account_number}/transactions"

    params = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "symbol": symbol,
        "types": types,
    }

    return client.request(url, params=params)


def get(account_number: str, transaction_id: int) -> Response:
    return client.request(
        f"{TRADER_URL}/accounts/{account_number}/transactions/{transaction_id}"
    )
