from tick.schwab.trader import user_preference


def test_user_preference():
    response = user_preference.get()
    assert response.status_code == 200
