import pytest

from tick.schwab.market_data import movers


@pytest.mark.parametrize("symbol", movers.Symbol)
def test_movers(symbol: movers.Symbol):
    response = movers.get(symbol)
    assert response.status_code == 200
