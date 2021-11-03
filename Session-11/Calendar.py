"""
Python defines an inbuilt module calendar that handles operations related to the calendar.
The calendar module allows output calendars like the program and provides additional useful
functions related to the calendar.
These calendars have Monday(0) as the first day of the week, and Sunday(6) as the last.

month() :
    This function prints the month of a specific year mentioned in arguments. It takes 4 arguments, year,
month,width of characters and no. of lines taken by a week.
"""
import calendar as c

print(c.month(2021, 11), type(c.month(2021, 11)))
print('\n')

"""
calendar()
    calendar(year, w, l, c):- This function displays the year, the width of characters,
    no. of lines per week,and column separations.
"""

print(c.calendar(2012, 3, 1, 5))
print('\n')

"""
isleap (year):  This function checks if the year mentioned in the argument is a leap or not.
"""

print(c.isleap(2014))
print(c.isleap(2020))
print('\n')

"""
 leapdays (year1, year2):  This function returns the number of leap days between the specified 
years in arguments.
"""

print(c.leapdays(2000, 2021))
print('\n')

"""
monthrange(year, month) : This function returns two integers, first, the starting day number of week
(0 as monday),second, the number of days in the month.
"""

print(c.monthrange(2021, 11))
print('\n')

"""
weekday(year, month, date) :- This function returns the week day number(0 is Monday) of the date 
specified in its arguments.
"""

print(c.weekday(2021, 11, 3))
print('\n')

"""
class calendar.Calendar : 
The calendar class creates a Calendar object. A Calendar object provides several methods that can be used
for preparing the calendar data for formatting.

iterweekdays()	Returns an iterator for the week day numbers that will be used for one week
itermonthdates()	Returns an iterator for the month (1–12) in the year
"""

obj = c.Calendar(firstweekday=6)

for day in obj.iterweekdays():
    print(day)


"""
class calendar.TextCalendar :
    TextCalendar class can be used to generate plain text calendars.
    
few functions in TextCalendar
formatmonth()	Method is used to get month’s calendar in a multi-line string\

"""