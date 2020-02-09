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
error = []
def input_date():
    #for line in fileinput.input():
    #    pass
    #date = input("Enter Date: ")
    pass


class DayFormat:
def check_day_format(day):
    if not (int):
        return False
    else:
    if not (0 < day <= 31):
        #if leap year then
        return False
    else:
    if(day > 2):
        return False
    else:
        return True

    # day_RegEx = re.compile("r^(([0]?[1-9])|([1-2][0-9])|(3[01]))$")
    # if day_RegEx.match(day):
    #     print("Yes")
    #     return True
    # else:
    #     print("No")
    #     return False
        # append error
    # if feb 29 and not leap year -> error
    # if 31 and not 31 month -> error

class MonthFormat:
def check_month_format(month):
    month_RegEx = re.compile("((0[1-9]|1[0-2])/([01][1-9]|10|2[0-8]))|((0[13-9]|1[0-2])/(29|30))|((0[13578]|1[0-2])/31)")
    if month_RegEx.match(month):
        return True
    else:
        return False

class YearFormat:
    def check_year_format(year):
        year_RegEx = re.compile("(?<!\d)\d{4}(?!\d)")
        if year_RegEx.match(year):
            return True
        else:
            return False

    def leap_year(year):
        print(year)
        if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
            print("leap year")
        else:
            print("not leap year")

    def range_date(year):
        if 1753 < year > 3000:
            return True
        else:
            return False

if __name__ =='__main__':
    for date in sys.stdin:
        res = re.split(r'[\-/\s]', date)
        try:
        day, month, year, _ = res
        except:

        print(day)
        error = []
        check_day_format(int(day))
        # check_month_format(month)
        # check_year_format(year)
        # leap_year(int(year))
        #range_date(year)