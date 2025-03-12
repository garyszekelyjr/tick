import pytest

from tick.schwab.market_data import market_hours


def test_markets():
    response = market_hours.get()
    assert response.status_code == 200


@pytest.mark.parametrize("market", market_hours.Market)
def test_market(market: market_hours.Market):
    response = market_hours.get(market)
    assert response.status_code == 200
