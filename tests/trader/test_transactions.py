from datetime import datetime

from tick import TZ
from tick.schwab.trader import transactions


def test_transactions(account_numbers):
    start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
    end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
    for account_number in account_numbers:
        response = transactions.get_all(
            account_number["hashValue"], start_date, end_date
        )
        assert response.status_code == 200


def test_transaction(account_numbers):
    start_date = datetime(2025, 1, 1, 0, 0, 0, 0, TZ)
    end_date = datetime(2025, 12, 31, 23, 59, 59, 999999, TZ)
    for account_number in account_numbers:
        response = transactions.get_all(
            account_number["hashValue"], start_date, end_date
        )
        assert response.status_code == 200
        transaction = response.json()[0]
        if transaction:
            response = transactions.get(
                account_number["hashValue"], transaction["activityId"]
            )
            assert response.status_code == 200
