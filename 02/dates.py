import fileinput
import re
import sys

#valid_date = re.compile(r'^(([0]?[1-9])|([1-2][0-9])|(3[01]))$')


month_RegEx = re.compile(r'^(0?[1-9]|[1][02]|JAN|Jan|FEB|Feb|MAR|Mar|APR|Apr|MAY|May|JUN|Jun|JUL|Jul|AUG|Aug'
  r'|SEP|Sep|OCT|Oct|NOV|Nov|DEC|Dec)$')


#error = []

def check_day_format(day):
    """
    A method that checks the day format between the ranges of 01-31
    DayFormat: DD or D or 0D

    :param day:
    :return boolean: Whether or not the day is within the correct range
    """
    day_RegEx = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-9]|[3][0-1])$')
    if day_RegEx.match(day):
        return True
    else:
        print("Wrong day range")
        return False

def check_month_format(month):
    """
    A method that checks the month format
    MonthFormat: MM or M or 0M or first 3 letters MMM

    :param month:
    :return boolean: Whether or not the month is in the correct format
    """
    if month_RegEx.match(month):
        return True
    else:
        return False

def check_year_format(year):
    """
    A method that checks the year format
    YearFormat: YY or YYYY

    :param year:
    :return boolean: Whether or not the year is the correct format
    """
    if len(year) == 4 and 1753 <= int(year) <= 3000:
        return True
    else:
        if len(year) == 2: # is_two_digits.match(year)
            return True
        else:
            print("Wrong year")
            return False

def leap_year(year):
    """
    A method that checks if it is a leap year or not

    :param year:
    :return boolean: Whether or not it is a leap year
    """
    year_int = year
    is_two_digits = re.compile(r'\d{2}')
    if is_two_digits.match(year):
        if 59 <= int(year) <= 99:
            year_int = 1900 + int(year)
        else:
            year_int = 2000 + int(year)

    if year_int % 4 == 0 and (year_int % 400 == 0 or year_int % 100 != 0):
        return True
    else:
        return False

# def range_date(year):
#     """
#     A method that checks if the year falls within the correct range
#
#     :param year:
#     :return boolean: Whether or not its within the correct range
#     """
#     if 1753 < year > 3000:
#         print("out of range")
#         return True
#         print("within range")
#     else:
#         return False
#     if 00 <= year >= 99:
#         print("win range")
#     else:
#         print("out of range")


def is_29_feb(day, month):
    """
    A method that accounts for the 29 of Feb, and if it is in the correct format
    DayFormat_29: DD

    :param day:
    :param month:
    :return boolean: whether of not it is a leap year
    """
    feb_regex = re.compile(r'^(0?[2]|FEB|Feb)$')
    if feb_regex.match(month) and 29 == int(day):
        return True
    else:
        return False


def check_day_range(day, month, year):
    """
    Checks if day is within valid range and accounts for Feb29(leap years)

    :param day:
    :param month:
    :return boolean: whether its within correct range
    """
    thirty_month = re.compile(r'^(0?[4]|0?[6]|0?[9]|11|APR|Apr|JUN|Jun|SEP|Sep|NOV|Nov)$')
    feb_regex = re.compile(r'^(0?[2]|FEB|Feb)$')
    below_29 = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-8])$')
    below_31 = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-9]|30)$')

    if (thirty_month.match(month) and not(below_31.match(day))) or (feb_regex.match(month) and not(below_29.match(day))):
        if is_29_feb(day, month) and leap_year(year):
            return False
        else:
            return True
    else:
        return False


curr_date = ""

def main():
    """
    Main driver control of program. Prompts user for input
    Control flow of program is to split the 'day', 'month' and 'year'
    and then passes each value to the respective methods which checks
    both the format and conditions of each

    :return: None
    """
    print("Enter Date:")
    for date in sys.stdin:
        if date[0] == ' ':
            print("Starts with white space")
            continue
        date = date.strip('\n')
        res = re.split(r'[\-/\s]', date)
        curr_date = date
        try:
            day, month, year = res
        except ValueError:
            print("Wrong Separator or unsupported format")
            continue
        try:
            (len(res) == 3)
        except ValueError:
            print("Wrong input")

        if check_day_format(day) and check_month_format(month) and check_year_format(year):
            if is_29_feb(day, month) and not (leap_year(year)):
                print("ERROR: year must be leap year")
            elif check_day_range(day, month, year):
                print("wrong day range")
            else:
                print("Correct")

if __name__ =='__main__':
    main()
