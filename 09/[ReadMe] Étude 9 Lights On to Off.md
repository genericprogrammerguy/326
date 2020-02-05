[ReadMe] Étude 9 Lights On to Off  
===
**Authors:** Nathaniel Price, Stefan Walker
**Date:** 05/02/2020


## Introduction

The “Lights On to Off” etude is based around the scenario that you have recently purchased a new home, in which the electrician has left all the lights on, however while wiring the house he/she has associated some switches to lights in other rooms. The optimal goal to this problem is to find a solution that requires minimal amount of steps (flicking the switch on/off) as possible such that all the lights are off at the end. The problem was first termed by K. Sunter (1989), known as “The All-Ones Problem" [1]

## Actvity Log
Tue, 14 Jan - Research & Report | Stefan
Fri, 24 Jan - Workings & Report | Stefan & Nathaniel
Mon, 27 Jan - Research & Report | Stefan & Nathaniel
Tue, 28 Jan - Research & Email report | Stefan & Nathaniel
Tue, 04 Feb - Coding | Nathaniel
Wed, 05 Feb - Coding,Testing & ReadMe | Nathaniel & Stefan

## Amendments to Report
Our report detailed a number of methods for finding a solution. The method implemented here is a variant of the matrix equation method detailed in the report. In the report, it was mentioned that a certain subclass of this problem, namely circuits with non-invertible/singular adjacency matrices, could not be solved via Gaussian elimination. Since the report, we discovered that the issue does not actually arise when using Gaussian eliminaton over the binary Galois Field, also known as GF(2). Furthermore, we found a function written in Python in which Gaussian elimination of matrices in GF(2) was implemented (see GF2_Gauss.py in Methods)[2]. We decided to use this function in our program, adapting it slightly for our needs.


Although this method was found to consistently result in a correct solution, it was also discovered that the order in which the lights in a certain problem were labelled (e.g. if light A was renamed B and vice versa) could affect the solution, sometimes resulting in multiple different solutions to what was essentially the same problem (i.e. the graph of the problem, before labelling nodes, was identical). Since some of these solutions may require more steps, our program cannot be guaranteed to return the minimal result, though no solution generated will require a given switch to be pressed more than once, so the solutions are relatively minimal. To find the absolute minimal solution for a given problem, every permutation (in terms of how lights are labelled) would have to be compared, which would slow the program down excessively for large input, hence why we did not implement this.

## Running the program
The program is .py file which includes [Lights_On_To_Off.py] it also imports [GF2_Gauss.py] it also includes a tesfile [testfile.txt] 

To run the program with file input

```python Lights_On_To_Off.py < testfile.txt```

To get a full print off of the matrices use the flag 

```-Steps```

To quit the program, enter ```&Q``` (either at the end of the file or manually in terminal)

The program imports the NumPy library (usually included with Python install)

Input must be given as follows:
example:
line 1: ```$A B C``` lights in circuit
line 2: ```$AB BA AC``` connections in circuit (AB is A->B)

## Methods

### Lights_On_To_Off.py  
 
#### Fill_matrix():
Creates the adjacency matrix from the lists of nodes and links

#### Get_answer():
Runs GF2_Gauss 

#### Print_state():
Prints out an adjancency matrix

#### Try_answer(): 
Determines whether the result is a valid solution and prints the checking steps if run with -Steps

#### Print_answer():
Displays the output to user of final adjancency matrix

#### Reset(self):
Resets adjancency matrix and other variables 

#### main()
Runs the main program. Also prints out the number of connections etc.. 

### GF2_Gauss.py
Is a script used to do Gaussian elimination for binary matrices

this code was adapted from: https://gist.github.com/popcornell/bc29d1b7ba37d824335ab7b6280f7fec


## References

[1] Sutner, K. Linear cellular automata and the garden-of-eden. The Mathematical Intelligencer 11, 49–53 (1989). https://doi.org/10.1007/BF03023823
[2] Samuele Cornell https://gist.github.com/popcornell/bc29d1b7ba37d824335ab7b6280f7fec