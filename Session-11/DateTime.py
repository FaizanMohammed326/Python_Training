"""
Python Datetime module supplies classes to work with date and time. These classes provide a number of
functions to deal with dates, times and time intervals.

Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects
  and not string or timestamps.

The DateTime module is categorized into 6 main classes
1.date:
     Its attributes are year, month and day.
2.time:
    Its attributes are hour, minute, second, microsecond, and tzinfo.
3.datetime:
   Its a combination of date and time along with the attributes year, month, day, hour, minute, second,
microsecond, and tzinfo.
4.timedelta:
    A duration expressing the difference between two date, time, or datetime instances to microsecond
resolution.
5.tzinfo:
    It provides time zone information objects.
6.timezone – A class that implements the tzinfo abstract base class as a fixed offset from the UTC
"""
from datetime import date
from datetime import time
from datetime import datetime, timedelta
from pytz import timezone

"""
1.date :
    The date class is used to instantiate date objects in Python.
When an object of this class is instantiated,it represents a date in the format YYYY-MM-DD
"""

my_date = date(1996, 12, 11)
print("my_date : ", my_date)

today = date.today()
print("today`s date : ", today)

print("Current year : ", today.year)
print("Current month : ", today.month)
print("Current day : ", today.day)

Str = date.isoformat(today)
print("String format : ", Str)
print(type(Str))

today = today.replace(2021, 11, 4)
print("after replacing : ", today)
print("\n")

"""
time:
    The time class creates the time object which represents local time, independent of any day.
Syntax:
    class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0) 
"""

my_time = time(13, 24, 56)
print("Entered time : ", my_time)
my_time = time(minute=12)
print("Time with one argument : ", my_time)
my_time = time()
print("Time without argument : ", my_time, "\n")

Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)
Str = Time.isoformat()
print("String Representation:", Str)

Time = Time.replace(minute=44)
print("Time after updating : ", Time)
print("\n")

"""
datetime
    The DateTime class contains information on both date and time.
Syntax:
class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0) 
"""

a = datetime(1999, 12, 12)
print(a)

a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

now = datetime.now()
print("Current date and time is : ", now)

string = datetime.isoformat(now)
print(string)
print(type(string))

today = date.today()
print("today Date object : ", today)
cur_time = datetime.time(now)
print("current Time  object : ", cur_time)
new = datetime.combine(today, cur_time)
print("combined time and date : ", new)
print("\n")

"""
Timedelta class:
    Python timedelta class is used for calculating differences in dates and also can be used for
date manipulations in Python. It is one of the easiest ways to perform date manipulations.

Syntax:
    class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
Returns : Date 

Add days to datetime object:

"""
time_now = datetime.now()
print("initial_date", time_now)

date_after_2yrs = time_now + timedelta(days=730)
print('future_date_after_2yrs:', date_after_2yrs)

print(-timedelta(days=340, hours=16))

dif_time = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(time_now - dif_time)
print(timedelta(days=365)/2)
print("\n")

"""

Formatting Datetime can be very necessary as the date representation may different from place to place.
strftime() method converts the given date, time or datetime object to the a string representation 
of the given format.

%a	    Abbreviated weekday name.	
%A	    Full weekday name.
%w	    Weekday as a decimal number.
%d	    Day of the month as a zero added decimal.
%-d	    Day of the month as a decimal number.
%b	    Abbreviated month name.
%B	    Full month name.
%m	    Month as a zero added decimal number.
"""

now = datetime.now()
print("Without formatting", now)

s = now.strftime("%A %m %Y")
print('\nExample 1:', s)
print("\n")

"""
Timezone:
    Timezones in DateTime can be used in the case where one might want to display time according to the
timezone of a specific region.

This can be done using the pytz module of Python.
This module serves the date-time conversion functionalities and helps users serving international client bases.
"""
now = datetime.now()
now_utc = now.astimezone(timezone('UTC'))
print("current time in UTC : ", now_utc)

now_ny1 = now.astimezone(timezone('America/New_York'))
now_ny2 = now_utc.astimezone(timezone('America/New_York'))
print("time in New York from : ", now_ny1)
print(now_ny2)
