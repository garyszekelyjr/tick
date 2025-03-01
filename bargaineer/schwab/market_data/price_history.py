from datetime import datetime
from enum import Enum

from requests import Response

from .. import client
from bargaineer.schwab.market_data import MARKET_DATA_URL


class PeriodType(Enum):
    DAY = "day"
    MONTH = "month"
    YEAR = "year"
    YTD = "ytd"


class DayPeriod(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    TEN = 10


class MonthPeriod(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    SIX = 6


class YearPeriod(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FIVE = 5
    TEN = 10
    FIFTEEN = 15
    TWENTY = 20


class YTDPeriod(Enum):
    ONE = 1


class FrequencyType(Enum):
    MINUTE = "minute"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"


class MinuteFrequency(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    FIFTEEN = 15
    THIRTY = 30


class DailyFrequency(Enum):
    ONE = 1


class WeeklyFrequency(Enum):
    ONE = 1


class MonthlyFrequency(Enum):
    ONE = 1


def price_history(
    symbol: str,
    start_date: datetime,
    end_date: datetime,
    need_extended_hours_data: bool = False,
    need_previous_close: bool = False,
    period_type: PeriodType | None = None,
    period: DayPeriod | MonthPeriod | YearPeriod | YTDPeriod | None = None,
    frequency_type: FrequencyType | None = None,
    frequency: MinuteFrequency
    | DailyFrequency
    | WeeklyFrequency
    | MonthlyFrequency
    | None = None,
) -> Response:
    url = f"{MARKET_DATA_URL}/pricehistory"
    params = {
        "symbol": symbol,
        "startDate": int(start_date.timestamp() * 1000),
        "endDate": int(end_date.timestamp() * 1000),
        "needExtendedHoursData": str(need_extended_hours_data).lower(),
        "needPreviousClose": str(need_previous_close).lower(),
    }
    if period_type:
        params["periodType"] = period_type.value
    if period:
        params["period"] = period.value
    if frequency_type:
        params["frequencyType"] = frequency_type.value
    if frequency:
        params["frequency"] = frequency.value
    return client.request(url, params=params)
