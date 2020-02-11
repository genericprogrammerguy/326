import fileinput
import re
import sys

#valid_date = re.compile(r'^(([0]?[1-9])|([1-2][0-9])|(3[01]))$')
#if valid_date.match(12):
#    print("nice")
# date = "22 10/90"
# res = re.split(r'[\-/\s]', date)
# print(res)
# exit(0)

monthDic = {1: 'JAN', 2: 'FEB', 3: 'MAR', 4: 'APR', 5: 'MAY', 6: 'JUN', 7: 'JUL', 8: 'AUG', 9: 'SEP', 10: 'OCT',
         11: 'NOV', 12: 'DEC'}

month_RegEx = re.compile(r'^(0?[1-9]|[1][02]|JAN|Jan|FEB|Feb|MAR|Mar|APR|Apr|MAY|May|JUN|Jun|JUL|Jul|AUG|Aug'
  r'|SEP|Sep|OCT|Oct|NOV|Nov|DEC|Dec)$')


error = []

#class DayFormat:
# int = 01
def check_day_format(day):
    # if 0 < day <= 31:
    #     # print("correct digits")
    #     return True
    # else:
    #     return False
    day_RegEx = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-9]|[3][0-1])$')
    if day_RegEx.match(day):
        return True
    else:
        print("wrong day range")
        return False



#class MonthFormat: MM or M or 0M or first 3 letters MMM
def check_month_format(month):
    if month_RegEx.match(month):
        return True
        # print("correct month")
    else:
        return False
        # print("wrong month")
    # if len(month) >=3:
    #     print("Too many digits-month")
    #     return False
    # else:
    #     print("Correct digits")
    #     return True

    # only up to 12
    # if month is string
    #     check >4 char
    #     Check month aginast monthDic
    #
    #     monthConverter()
    # check reference dictionary of months (3 Letters)
        # check consist of alphabetic
        # invalid month
        # invalid number of Char(3)

        # Not # letters


#class YearFormat:
def check_year_format(year):
    # year_RegEx = re.compile(r'\d{4}$')
    # is_two_digits = re.compile(r'\d{2}')
    # if year_RegEx.match(year) and 1753 <= int(year) <= 3000:
    #     print("correct year")
    #     return True
    # else:
    #     print("wrong year")
    #     return False
    if len(year) == 4 and 1753 <= int(year) <= 3000:
        return True
    else:
        if len(year) == 2: # is_two_digits.match(year)
            return True
        else:
            print("wrong year")
            return False

def leap_year(year):
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

def range_date(year):
    if 1753 < year > 3000:
        print("out of range")
        return True
        print("in range")
    else:
        return False
    if 00 <= year >= 99:
        print("in range")
    else:
        print("out range")


def is_29_feb(day, month):
    # try:
    #     cvt = int(month)
    #     if cvt == 2:
    #         return True
    # except ValueError:
    #     pass

    feb_regex = re.compile(r'^(0?[2]|FEB|Feb)$')
    # day_RegEx = re.compile(r'^(0?[2])$')
    if feb_regex.match(month) and 29 == int(day):
        return True
    else:
        return False


def check_day_range(day, month):
    """
    Returns True if range is wrong
    :param day:
    :param month:
    :return:
    """
    # april 4 , june 6 , sep, 9  nov 11
    thirty_month = re.compile(r'^(0?[4]|0?[6]|0?[9]|11|APR|Apr|JUN|Jun|SEP|Sep|NOV|Nov)$')
    feb_regex = re.compile(r'^(0?[2]|FEB|Feb)$')
    below_29 = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-8])$')
    below_31 = re.compile(r'^(0?[1-9]|[1][0-9]|[2][0-9]|30)$')

    if (thirty_month.match(month) and not(below_31.match(day))) or (feb_regex.match(month) and not(below_29.match(day))):
        return True
    else:
        return False



if __name__ =='__main__':
    print("Date:")
    for date in sys.stdin:
        if date[0] == ' ':
            print("starts with white space")
            continue
        date = date.strip('\n')
        res = re.split(r'[\-/\s]', date)
        try:
            day, month, year = res
        except ValueError:
            print("wrong seperator")
            continue

        if check_day_format(day) and check_month_format(month) and check_year_format(year):
            if is_29_feb(day, month) and not(leap_year(year)):
                print("ERROR: year must be leap year")
            elif check_day_range(day, month):
                print("wrong day range")
            else:
                print("All is correct")
    # leap years, months that are 30 or 31
    #
        #leap_year(int(year))
        #range_date(int(year))