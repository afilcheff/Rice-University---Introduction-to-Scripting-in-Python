"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime
from datetime import date

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    input_date = datetime.date(year, month, 1)
    if year == 9999 and month == 12:
        return 31
    elif month == 12:
        dummy_date = datetime.date(year + 1, 1, 1)
    else:
        dummy_date = datetime.date(year, month + 1, 1)
    
    days_in_month = abs(input_date - dummy_date)
    days_in_month = days_in_month.days
    return days_in_month

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR and 1 <= month <= 12 and 0 < day <= days_in_month(year, month):
        return True
    else:
        return False
    
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        if date1 > date2:
            return 0
        else:
            days_diff = abs(date1 - date2)
            days_diff = days_diff.days
            return days_diff
    else:
        return 0

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if not is_valid_date(year, month, day):
        return 0
    else:
        birthday = datetime.date(year, month, day)
        today = date.today()
        if today > birthday:
            return 0
        days_diff = abs(today - birthday)
        days_diff = days_diff.days
        return days_diff
            
print(age_in_days(1993, 9, 15))
