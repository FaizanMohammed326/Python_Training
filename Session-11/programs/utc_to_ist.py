# WAP to convert datetime to utc and ist timezone

from datetime import datetime, timedelta
from pytz import timezone


def toUTC(dt):
    UTC_datetime = dt.astimezone(timezone('UTC'))
    print("given time in UTC :", UTC_datetime)
    return UTC_datetime


def toIST(dt):
    IST_datetime = dt.astimezone(timezone('Asia/Kolkata'))
    print("given time in UTC :", IST_datetime)
    return IST_datetime


cur_time = datetime.now()
UTC = toUTC(cur_time)
IST = toIST(UTC)
