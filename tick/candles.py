import mplfinance as mpf
import pandas as pd

from tick.schwab.market_data import price_history


TICKER = "SPY"

response = price_history.get(
    TICKER,
    period_type=price_history.PeriodType.DAY,
    period=price_history.DayPeriod.ONE,
    frequency_type=price_history.FrequencyType.MINUTE,
    frequency=price_history.MinuteFrequency.ONE,
)

candles = response.json()["candles"]

df = pd.DataFrame(candles).set_index("datetime")
df.index = pd.to_datetime(df.index, utc=True, unit="ms").map(
    lambda x: x.tz_convert("EST")
)

mpf.plot(df, type="candle", volume=True, style="yahoo", mav=(5, 10))
