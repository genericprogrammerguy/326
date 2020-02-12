[ReadMe] Étude 4 - Hilbert Curve
===
**Authors:** Stefan Walker
**Date:** 09/02/2020
**Version:** 1.0

## Introduction
Is a program that recursively draws the Hilbert curve, which will resize when the user clicks the mouse. 

I looked at a number of implementations on how the Hilbert curve can be done including:
* http://www.socouldanyone.com/2013/04/hilbert-curve-in-python-and-image.html
* https://www.khanacademy.org/computer-programming/hilbert-curve/803217159
* http://people.cs.aau.dk/~normark/prog3-03/html/notes/fu-intr-2_themes-hilbert-sec.html
* http://www.fundza.com/algorithmic/space_filling/hilbert/basics/
* https://rosettacode.org/wiki/Hilbert_curve#Recursive


It contains the following files:
* hilbert.py

## Running the program 

 
run the following terminal command:

```
python3 hilbert.py
```

## Methods

### def hilbert(t,dir, rot, order):
A method to recursively call the drawing of the Hilbert Curve

Example of order 1 

                 D----------------C
                                  |
                                  |
                                  |
                                  |
                                  |
                                  |
                 A----------------B


    
### def rescale(x,y):
Rescales the Hilbert curve when prompted from user input from the mouse. This method was chosen for a more interactive approach and because it gives the user the option to rescale 

### def main():
Prompts user for input of the order of magnitude for Hilbert curve.Then sets the turtle environment up and then recursively draws the Hilbert curve rescaling the screen from user input from the mouse

## References
[1] En.wikipedia.org. (2020). Space-filling curve. [online] Available at: https://en.wikipedia.org/wiki/Space-filling_curve [Accessed 1 Feb. 2020].

[2] recursion, D. (2020). Draw a Hilbert curve by recursion. [online] Stack Overflow. Available at: https://stackoverflow.com/questions/43230399/draw-a-hilbert-curve-by-recursion [Accessed 12 Feb. 2020].
