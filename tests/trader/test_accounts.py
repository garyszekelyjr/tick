import pytest

from tick.schwab.trader import accounts


def test_account_numbers():
    response = accounts.account_numbers()
    assert response.status_code == 200


def test_accounts():
    response = accounts.get_all()
    assert response.status_code == 200


def test_account():
    response = accounts.account_numbers()
    assert response.status_code == 200
    account_numbers = response.json()
    for account_number in account_numbers:
        response = accounts.get(account_number["hashValue"])
        assert response.status_code == 200
