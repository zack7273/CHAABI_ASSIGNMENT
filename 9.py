"""
Q9.
Write a func that takes 3 args:
from_date - string representing a date in the form of 'yy-mm-dd'
to_date - string representing a date in the form of 'yy-mm-dd'
difference - int
Returns True if from_date and to_date are less than difference days away from each other, else
returns False.
"""

from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert string dates to datetime objects
    from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
    to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between dates
    date_diff = abs((to_date_obj - from_date_obj).days)

    # Check if the difference is less than the specified value
    if date_diff < difference:
        return True
    else:
        return False

from_date = '21-01-01'
to_date = '21-01-10'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)  # Output: True




"""


from datetime import datetime, timedelta

This line of code imports the datetime and timedelta classes from the datetime module. The datetime class represents a date and time, and the timedelta class represents a time interval.


def check_date_difference(from_date, to_date, difference):

This line of code defines a function called check_date_difference(). The function takes three arguments: a string representing the start date, a string representing the end date, and an integer representing the maximum difference between the two dates.


# Convert string dates to datetime objects
from_date_obj = datetime.strptime(from_date, '%y-%m-%d')
to_date_obj = datetime.strptime(to_date, '%y-%m-%d')

This code converts the two string dates to datetime objects. The datetime.strptime() function takes a string representing a date and time and a format string and returns a datetime object. The format string tells the datetime.strptime() function how to interpret the string. In this case, the format string is '%y-%m-%d', which means that the year, month, and day are separated by hyphens.


# Calculate the difference between dates
date_diff = abs((to_date_obj - from_date_obj).days)

This code calculates the difference between the two datetime objects. The - operator subtracts the two datetime objects. The abs() function returns the absolute value of the difference.


# Check if the difference is less than the specified value
if date_diff < difference:
    return True
else:
    return False

This code checks if the difference between the two dates is less than the specified value. If the difference is less than the specified value, the function returns True. Otherwise, the function returns False.


from_date = '21-01-01'
to_date = '21-01-10'
difference = 10

result = check_date_difference(from_date, to_date, difference)
print(result)  # Output: True

This code assigns the strings '21-01-01' and '21-01-10' to the variables from_date and to_date, respectively. The code assigns the integer 10 to the variable difference. The code calls the check_date_difference() function with the arguments from_date, to_date, and difference. The code prints the result of the check_date_difference() function. The output of the code is True.

"""
