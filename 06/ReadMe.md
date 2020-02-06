[ReadMe] Étude 7 - Graphical User Interface 
===
**Authors:** Nathaniel Price, Stefan Walker
**Date:** 06/02/2020
**version** 1.0 


## Introduction
To build and implement a Graphical User Interface(GUI) which gives a visualisation of the operations performed on the chosen data structure to aid other students in the understanding of the chosen data structure. Excellent existing examples can be found at the [University of San Francisco](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html).


The data structure we have chosen is a [linked list](https://en.wikipedia.org/wiki/Linked_list).

## Activity Log
Tue, 28 Jan - Design and Planning | Stefan
Thu, 30 Jan- Planning | Stefan
Sun, 2 Feb - Coding | Stefan
Tue, 4 Feb - Coding | Stefan
Wed, 5 Feb - Coding | Stefan
Thu, 6 Feb - Coding | Nathaniel
Thu, 6 Feb - ReadMe | Stefan

## Running the Program 
To run from terminal, type the following into the terminal:

```
$python3 Gui.py
```
Alternatively, to run from IDLE3.5 (Python), type the following into the terminal:
```
$IDLE3.5 Gui.py
```
Then, once the code has opened in IDLE, press F5 to run the program.

## Methods
The methods to implement include in the Linked list include:  
-[Push](https://https://www.geeksforgeeks.org/linkedlist-push-method-in-java/) 
-[Pop](https://https://www.geeksforgeeks.org/linkedlist-pop-method-in-java/)
-[Search](https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive)(value)
-Traverse(index)
-Add(After)
-[Delete](https://https://www.geeksforgeeks.org/write-a-function-to-delete-a-linked-list/)

### Class LinkedList
An implementation class of a linked list, containing several methods 

##### def insert_after
A method that inserts a value at a specific index location

##### def delete_after
A method that deletes a value at index (n+1) value location

#### def push_front
A method that places a value at the start of the link list 

#### def pop_front
A method that removes a value at the front of link list

#### def push_back 
A method that removes a value at the back of the link list

#### def pop_back
A method that removes a value at the back of the link list

#### def traverse
A method that moves to the specific index location of the link list

#### def search
A method that searches the link list for the specific value and display it on   

### class AppWindow:
Runs the main program and generates the graphical display on screen  

## References & Resources  
[Fahrenheit to Celsius Python GUI](https://https://www.youtube.com/watch?v=H1-6DfphTKQ&list=PL6lxxT7IdTxGoHfouzEK-dFcwr_QClME_&index=30)  