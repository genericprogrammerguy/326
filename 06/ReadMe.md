[ReadMe] Étude 6 - Counting it Up 
===
**Authors:** Nathaniel Price, Stefan Walker
**Date:** 04/02/2020
**Version:** 1.0
**Git:** [5c4ba0b](https://github.com/non-emulated-programmer/326/commit/5c4ba0bf684e2d3b910a6431f77135e703e5f225)



## Introduction
----
This is a basic computer program which takes an input of 64-bit integers computes the value of (f) for given n and k, and then outputs a 64-bit interger. 

**For example:**
Output for the value of 
(n k) = (52 5) = 52! / 5!(52−5)! = 2598960
 

It contains the following files:
* CountingApp.java
* CountingApp.class
* testfile.txt

## Actvity Log
Tue, 21 Jan - Research| Stefan
Mon, 27 Jan - Workings | Stefan & Nathaniel
Sat, 01 Feb - Coding | Nathaniel
Sun, 02 Feb - Coding | Nathaniel
Tue, 04 Feb - Testing | Stefan & Nathaniel
Tue, 04 Feb - ReadMe | Stefan
Wed, 05 Feb - Refactoring | Stefan

## Running the program 
---
Unzip the file

Then to run this program cd into the directory containing the files. 

Then run the following terminal command:

```
java CountingApp
```
Running the following command: 

```
java CountingApp < testfile.txt
```
will pass testfile.txt into the program  

testfile.txt contains a number of inputs which test the program for a number of different inputs

## Methods
### public static void main 
Runs the main program and takes input from [system.in](https://docs.oracle.com/javase/7/docs/api/java/lang/System.html) 

### public String calculate( long n, long k ) ###
Takes 2 longs (n and k) and preforms the main calculation and returns a string

#### Long.toUnsignedString 
A method that returns a string representation of the argument as an unsigned decimal value.

#### Long.divideUnsigned
returns the unsigned quotient of dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.

#### Long.remainderUnsigned
returns the unsigned remainder from dividing the first argument by the second where each argument and the result is interpreted as an unsigned value.

#### Long.parseUnsignedLong
compares two long values numerically. Parses the string argument as an unsigned decimal long.

### public String multiplyLong(long x, long y) ###
Takes 2 longs (x and y) and returns the result of multpilying them together one digit at a time. The answer is stored as an array of digits and return type is String, since the answer may be greater than the maximum size for a signed long. 

**Adapted from:** https://stackoverflow.com/questions/35260827/implementing-multiplication-algorithm-in-java


### public boolean isAllDigit( String s )
Takes in a string and returns a boolean as to weather it is a digit 

### public long gcdByEuclidsAlgorithm(long n1, long n2)
Takes 2 longs (n and k) and finds the greatest common divisor and returns a long

**Adapted from:** https://www.baeldung.com/java-greatest-common-divisor

