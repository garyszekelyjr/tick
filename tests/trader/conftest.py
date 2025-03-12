import pytest

from tick.schwab.trader import accounts


@pytest.fixture(scope="session")
def account_numbers():
    response = accounts.account_numbers()
    assert response.status_code == 200
    return response.json()
