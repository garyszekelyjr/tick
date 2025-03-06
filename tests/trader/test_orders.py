from datetime import datetime

from tick import TZ
from tick.schwab.trader import accounts, orders

response = accounts.account_numbers()
assert response.status_code == 200
account_numbers = response.json()


def test_orders():
    from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
    to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
    response = orders.orders(from_entered_time, to_entered_time)
    assert response.status_code == 200


def test_accounts_orders():
    from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
    to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
    for account_number in account_numbers:
        response = orders.accounts_orders(
            account_number["hashValue"], from_entered_time, to_entered_time
        )
        assert response.status_code == 200


def test_accounts_order():
    from_entered_time = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
    to_entered_time = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
    for account_number in account_numbers:
        response = orders.accounts_orders(
            account_number["hashValue"], from_entered_time, to_entered_time
        )
        assert response.status_code == 200
        order = response.json()[0]
        if order:
            response = orders.accounts_order(
                account_number["hashValue"], order["orderId"]
            )
            assert response.status_code == 200
