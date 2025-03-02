from datetime import datetime
from enum import Enum
from typing import Dict, List

from requests import Response

from .. import client
from . import TRADER_URL


class Status(Enum):
    AWAITING_PARENT_ORDER = "AWAITING_PARENT_ORDER"
    AWAITING_CONDITION = "AWAITING_CONDITION"
    AWAITING_STOP_CONDITION = "AWAITING_STOP_CONDITION"
    AWAITING_MANUAL_REVIEW = "AWAITING_MANUAL_REVIEW"
    ACCEPTED = "ACCEPTED"
    AWAITING_UR_OUT = "AWAITING_UR_OUT"
    PENDING_ACTIVATION = "PENDING_ACTIVATION"
    QUEUED = "QUEUED"
    WORKING = "WORKING"
    REJECTED = "REJECTED"
    PENDING_CANCEL = "PENDING_CANCEL"
    CANCELED = "CANCELED"
    PENDING_REPLACE = "PENDING_REPLACE"
    REPLACED = "REPLACED"
    FILLED = "FILLED"
    EXPIRED = "EXPIRED"
    NEW = "NEW"
    AWAITING_RELEASE_TIME = "AWAITING_RELEASE_TIME"
    PENDING_ACKNOWLEDGEMENT = "PENDING_ACKNOWLEDGEMENT"
    PENDING_RECALL = "PENDING_RECALL"
    UNKNOWN = "UNKNOWN"


def orders(from_entered_time: datetime, to_entered_time: datetime) -> Response:
    url = f"{TRADER_URL}/orders"

    params = {
        "fromEnteredTime": from_entered_time.isoformat(),
        "toEnteredTime": to_entered_time.isoformat(),
    }

    return client.request(url, params=params)


def accounts_orders(
    account_number: str,
    from_entered_time: datetime,
    to_entered_time: datetime,
    status: str = "",
) -> Response:
    url = f"{TRADER_URL}/accounts/{account_number}/orders"
    params = {
        "fromEnteredTime": from_entered_time.isoformat(),
        "toEnteredTime": to_entered_time.isoformat(),
        "status": status,
    }
    return client.request(url, params=params)


def accounts_order(account_number: str, order_id: int) -> Response:
    return client.request(f"{TRADER_URL}/accounts/{account_number}/orders/{order_id}")


def post_order(
    account_number: str,
    order_type: str,
    session: str,
    duration: str,
    order_strategy_type: str,
    order_leg_collection: List[Dict],
) -> Response:
    url = f"{TRADER_URL}/accounts/{account_number}/orders"
    data = {
        "orderType": order_type,
        "session": session,
        "duration": duration,
        "orderStrategyType": order_strategy_type,
        "orderLegCollection": order_leg_collection,
    }
    return client.request(url, "POST", data=data)


def delete_order(account_number: str, order_id: int):
    return client.request(
        f"{TRADER_URL}/accounts/{account_number}/orders/{order_id}", "DELETE"
    )


def put_order(
    account_number: str,
    order_id: int,
    order_type: str,
    session: str,
    duration: str,
    order_strategy_type: str,
    order_leg_collection: List[Dict],
):
    url = f"{TRADER_URL}/accounts/{account_number}/orders/{order_id}"
    data = {
        "orderType": order_type,
        "session": session,
        "duration": duration,
        "orderStrategyType": order_strategy_type,
        "orderLegCollection": order_leg_collection,
    }
    return client.request(url, "PUT", data=data)
