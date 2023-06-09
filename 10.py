"""

Q10. Of date and days
Write a func that takes 2 args:
date - string representing a date in the form of 'yy-mm-dd'
n - integer
Returns the string representation of date n days before 'date'
E.g. f('16-12-10', 11) should return '16-11-29'

"""

import datetime


def get_date_days_before(date, n):


  # Convert the date string to a datetime object.
  date_obj = datetime.datetime.strptime(date, '%y-%m-%d')

  # Subtract n days from the datetime object.
  new_date_obj = date_obj - datetime.timedelta(days=n)

  # Convert the datetime object to a date string.
  new_date = new_date_obj.strftime('%y-%m-%d')

  # Return the new date string.
  return new_date


if __name__ == "__main__":
  date = "16-12-10"
  n = 11

  new_date = get_date_days_before(date, n)

  print(new_date)
"""
First, the import datetime statement imports the datetime module from the Python standard library. This module provides classes and functions for working with dates and times.

Next, the get_date_days_before() function is defined. This function takes two arguments: a date in the form of 'yy-mm-dd', and an integer. The function returns the string representation of the date n days before the given date.

The function first converts the date string to a datetime object using the datetime.datetime.strptime() function. This function takes two arguments: the date string and a format string. The format string tells the strptime() function how to interpret the date string. In this case, the format string is 'yy-mm-dd'.

Next, the function subtracts n days from the datetime object using the - datetime.timedelta(days=n) expression. The timedelta class represents a time interval. The days=n argument specifies that the time interval should be n days long.

Finally, the function converts the datetime object to a date string using the strftime() function. This function takes two arguments: the datetime object and a format string. The format string tells the strftime() function how to format the datetime object. In this case, the format string is 'yy-mm-dd'.

The if __name__ == "__main__": statement is a special statement that is only executed when the code is run as a script. This statement is used to test the get_date_days_before() function.

The date and n variables are assigned the values "16-12-10" and 11, respectively. The new_date variable is assigned the value of the get_date_days_before() function, which returns the string "16-11-29". Finally, the print(new_date) statement prints the new_date variable, which is the string "16-11-29".

"""


"""
First, the import datetime statement imports the datetime module from the Python standard library. This module provides classes and functions for working with dates and times.

Next, the get_date_n_days_before() function is defined. This function takes two arguments: a date in the form of 'yy-mm-dd', and an integer. The function returns the string representation of the date n days before the given date.

The function first converts the date string to a datetime object using the datetime.datetime.strptime() function. This function takes two arguments: the date string and a format string. The format string tells the strptime() function how to interpret the date string. In this case, the format string is 'yy-mm-dd'.

Next, the function subtracts n days from the datetime object using the - datetime.timedelta(days=n) expression. The timedelta class represents a time interval. The days=n argument specifies that the time interval should be n days long.

Finally, the function converts the datetime object to a date string using the strftime() function. This function takes two arguments: the datetime object and a format string. The format string tells the strftime() function how to format the datetime object. In this case, the format string is 'yy-mm-dd'.

The if __name__ == "__main__": statement is a special statement that is only executed when the code is run as a script. This statement is used to test the get_date_n_days_before() function.

The date and n variables are assigned the values "16-12-10" and 11, respectively. The new_date variable is assigned the value of the get_date_n_days_before() function, which returns the string "16-11-29". Finally, the print(new_date) statement prints the new_date variable, which is the string "16-11-29".

"""