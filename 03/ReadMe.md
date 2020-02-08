[ReadMe] Étude 3 -  Floating Point 
===
**Authors:** Nathaniel Price, Stefan Walker, Ali Morris, Simon Zhao
**Date:** 08/02/20
**Version:** 1.1


## What the Program Does
A program that reads a file from an IBM System/ 360-format floating point numbers and write them to a new file  in IEEE standard format. 


## Running the Program 

In the terminal type:

to compile:

```$javac IbmToIeee.java```

to run:

```$java IbmToIeee```

## Activity Log
Wed 17 Jan - Research | Stefan
Tue 21 Jan - Planning + Calculations | Ali, Stefan, Nathaniel & Simon
Wed 22 Jan - Planning + Calculations | Ali, Stefan, & Nathaniel
Thu 23 Jan - Planning + Calculations | Ali, Stefan,  & Nathaniel
Fri 31 Jan - Testing | Stefan & Simon
Wed 05 Feb - Readme | Stefan & Ali 
Thur 06 Feb - Formatting + bug fixes | Stefan

Ali wrote the covert method and readme
Nathaniel wrote the main method and the checkInput functions.
Simon wrote the special method.
Stefan did all the testing, readme.

## Methods

The conversion between the two formats for all values gave a formula of 4(x) - 257 - 2^(e-1) where x is the decimal value of the exponent in the ibm form and e is the number of bits required for the precision of the ieee format. All 4 cases can be calculated with this formula as well as any bounds or limits. 

We found precision issues in the 32 bit ibm format when converting to the 32 bit ieee format. Values where the exponent was larger than 96 in base 10 would be out of range for the ieee and numbers less than 32 would also cause that. To over come these, output of infinity for values too large and 0 for values too small. 

## Testing 

https://drive.google.com/file/d/1rSarQ9me6TNP7NM63NT68RYj0w3QYNk_/view?usp=sharing

## References

Stack Overflow. (2020). java - IBM-IEEE double-precision floating point byte conversion. [online] Available at: https://stackoverflow.com/questions/37982757/java-ibm-ieee-double-precision-floating-point-byte-conversion [Accessed 23 Jan. 2020].



