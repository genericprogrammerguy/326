[ReadMe] Étude 2 - Dates
===
**Authors:** Stefan Walker
**Date:** 11/02/2020
**Version:** 1.1

## Version Log:



| Version | Date | Comment |
| -------- | -------- | -------- |
| **1.0**     | 11-02-2020    | First version   |
| **1.1**     | 13/02/2020    | Slight adjustments to error messages +  print out what is wrong as per etude 


## Introduction
A basic program to handle various formats of a date. Including the following formats:
1. **Day Format:** DD or D or 0D
1. **Month Format:** MM or M or 0M or first 3 letters MMM
1. **Year Format:** YY or YYYY

It contains the following files:
* dates.py
* test.txt

## Running the program 
 
Run the following terminal command:
```
python3 dates.py < test.txt
```
will pass a test file of various tests



## Methods
### def check_day_format(day):
#### DayFormat: DD or D or 0D
A method that checks the day format between the ranges of 01-31 returns a boolean  to whether or not the day is within the correct format and range 

### def check_month_format(month): 
#### MonthFormat: MM or M or 0M or first 3 letters MMM
A method that checks the month format and returns a boolean whether or not the month is in the correct format and range 

### def check_year_format(year): 
A method that checks the year format and returns a boolean whether or not the year is the correct format 

### def leap_year(year):
A method that checks if it is a leap year or not and returns a boolean value to whether or not it is a leap year
   
### def range_date(year):
A method that checks if the year falls within the correct range

### def is_29_feb(day, month):
A method that accounts for the 29 of February, and if it is in the correct format returns a boolean whether or not it is a leap year

### def check_day_range(day, month, year):
Checks if day is within valid range and accounts for February 29(leap years)
  
### def main():
Main driver control of program. Prompts user for input Control flow of program is to split the 'day', 'month' and 'year'and then passes each value to the respective methods which checks both the format and conditions of each. preforms a number of checks

## References
[1]YouTube. (2020). Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex). [online] Available at: https://www.youtube.com/watch?v=K8L6KVGG-7o&t=2800s&app=desktop [Accessed 28 Jan. 2020].

[2]Stack Abuse. (2020). Converting Strings to datetime in Python. [online] Available at: https://stackabuse.com/converting-strings-to-datetime-in-python/ [Accessed Feb. 2019].

[3]Goyvaerts, J. (2020). Full Documentation to RegexMagic: The Regular Expression Generator. [online] Regexmagic.com. Available at: http://www.regexmagic.com/manual.html#xmppatterndatetime [Accessed 11 Feb. 2020].