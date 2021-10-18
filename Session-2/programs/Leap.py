#WAP to check if the given year is a leap year or not

year = int(input())
def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        print(year, "is a leap year.")
    elif (year % 100 == 0):
        print(year, "is not a leap year")
    elif (year % 400 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


leap_year(year)
