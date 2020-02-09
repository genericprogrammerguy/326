from datetime import *
import fileinput
import re
import sys

#valid_date = re.compile(r'^(([0]?[1-9])|([1-2][0-9])|(3[01]))$')
#if valid_date.match(12):
#    print("nice")

def main():
   while True:
    input = input("Enter Date")
            
    check_day_format(input)
    check_month_format(input)
    check_year_format(input)
    leap_year(input)
    range_date(input)

def input_date():
    for line in fileinput.input():
        pass

date = input("Enter Date: ") 

def check_day_format(date):
    day_RegEX = date
    day_RegEX = re.compile("^(([0]?[1-9])|([1-2][0-9])|(3[01]))$");
    if day_RegEX.match():
        print("correct-Day")
    else:
        print("wrong-Day")

def check_month_format(date):
    month_RegEx = date
    month_RegEx = re.compile("((0[1-9]|1[0-2])/([01][1-9]|10|2[0-8]))|((0[13-9]|1[0-2])/(29|30))|((0[13578]|1[0-2])/31)");
    if month_RegEx.match():
        print("correct-Month")
    else:
        print("wrong-Month")

def check_year_format(date):
    year_RegEx = date  
    year_RegEx = re.compile("(?<!\d)\d{2}{4}(?!\d)");
    if year_RegEx.match():
        print("correct-Year")
    else:
        print("wrong-Year")

def leap_year(date):
    year = date
    if year%4==0 and year%100 ==0:
        if year%400 !=0:
            print("valid year") 
        else:
            print("invaild year")

def range_date(date):
    year = date
    if year < 1753 or year > 3000:
        print ("out of range")