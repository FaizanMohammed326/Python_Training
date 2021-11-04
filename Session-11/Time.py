"""
 Python time module allows to work with time in Python. It allows functionality like getting the current time,
 pausing the Program from executing, etc.

The epoch is the point where the time starts, and is platform dependent. On Windows and most Unix systems,
the epoch is January 1, 1970, 00:00:00 (UTC)
To check what the epoch is on a given platform we can use time.gmtime(0).
"""
import time

print(time.gmtime(0))

"""
time.time() methods return the current time in seconds since epoch. It returns a floating-point number.
"""

curr = time.time()
print("Current time in seconds since epoch =", curr)

"""
time.ctime() function returns a 24 character time string but takes seconds as argument and computes time till
mentioned seconds. If no argument is passed, time is calculated till the present.
"""
curr = time.ctime(1627908313.717886)
print("Current time:", curr)
print(time.ctime())

"""
Execution can be delayed using time.sleep() method. This method is used to halt the program execution for the
time specified in the arguments.
"""

for i in range(3):
    time.sleep(1)
    print(i)
