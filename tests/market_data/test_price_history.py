from datetime import datetime

from tick.schwab.market_data import price_history


def test_price_history():
    response = price_history.get(
        "AAPL", start_date=datetime(2025, 1, 1), end_date=datetime(2025, 1, 2)
    )
    assert response.status_code == 200
