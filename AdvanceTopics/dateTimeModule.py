"""
In Python, date and time are not a data type of its own, but a module named datetime can be imported to work with the date as well as time.
Datetime module comes built into Python, so there is no need to install it externally.
Datetime module supplies classes to work with date and time.
These classes provide a number of functions to deal with dates, times and time intervals.
Date and datetime are an object in Python, so when you manipulate them, you are actually manipulating objects and not string or timestamps.

Note – If the argument is not an integer it will raise a TypeError and if it is outside the range a ValueError will be raised.
"""

# Python program to
# demonstrate date class

# import the date class
from datetime import date

# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range

# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of interger
#-------------------------------------------------------------------------------------------------------
# Current date

"""
To return the current local date today() function of date class is used. today() function comes with several attributes (year, month and day).
These can be printed individually.

"""

# Python program to
# print current date

from datetime import date

# calling the today
# function of date class
today = date.today()

print("Today's date is", today)

# Printing date's components
print("Date components", today.year, today.month, today.day)
#----------------------------------------------------------------------------------------
# Python program to
# demonstrate time class

from datetime import time

# calling the constructor
my_time = time(13, 24, 56)

print("Entered time", my_time)

# calling constructor with 1
# argument
my_time = time(minute=12)
print("\nTime with one argument", my_time)

# Calling constructor with
# 0 argument
my_time = time()
print("\nTime without argument", my_time)

# Uncommenting time(hour = 26)
# will rase an ValueError as
# it is out of range

# uncommenting time(hour ='23')
# will raise TypeError as
# string is passed instead of int
from datetime import time

Time = time(11, 34, 56)

print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)

#---------------------------------------------
from datetime import datetime

# Calling now() function
today = datetime.now()

print("Current date and time is", today) 