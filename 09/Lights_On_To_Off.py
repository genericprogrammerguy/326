import numpy as np
from sys import stdin
from sys import argv
from GF2_Gauss import *

class Lights_Puzzle:
    def __init__(self):
        self.nodes = [] #list to store nodes
        self.links = [] #list to store link instruction strings
        self.A = [] #list to store adjacency matrix
        self.result = [] #list to store result in binary
        self.possible = True #boolean to store whether the circuit is solveable                

    def Fill_matrix(self):
        for i in range(len(self.nodes)):
            self.A.append([]) #initialized A to have same number of rows as there are nodes
            for j in range(len(self.nodes)+1):
               self.A[i].append(0) #initializes A to have one more column than it has rows
        for link in self.links:
##            print(link)
            a = self.nodes.index(link[0])
            b = self.nodes.index(link[1])
            self.A[b][a] = 1 # for a link A->B, the matrix gets a 1 in columnA, rowB
        for i in range(len(self.nodes)):
            self.A[i][i] = 1
            self.A[i][len(self.nodes)] = 1
        for cell in self.A:
            if cell != 1:
                cell = 0

    def Get_answer(self):
        M_numpy = np.array(self.A)
        self.result = GF2_Gauss(M_numpy)[:,-1]

    def Print_state(self): #prints the current state of self to give solution steps
        print "Adjacency matrix: "
        print(self.A)
        print

    def Try_answer(self): #goes through the multiplication to show that answer works
        A_numpy = np.array(self.A)
        initial = A_numpy[:, -1]
        A_numpy = A_numpy[:, :-1]
        answer = list(self.result);
        to_print = ""
        if argv[len(argv)-1] == '-Steps': #shows proof of result if program is run with -Steps
            print
            print("Checking: ")
            print
            print(str(A_numpy) + " times " + str(self.result) + " equals " + str(initial))
            print
            for i in range(len(self.result)): #loop to print linear equation represented by matrix equation 
                for j in range(len(A_numpy[i])):
                    if A_numpy[i][j] == 1:
                        to_print = to_print + ((str(self.nodes[j]) + " + "))
                to_print = to_print[:-2]
                print(to_print + " = " + str(list(initial)[i])) #not sure if thi one is right
                print
                to_print = ""
            print((A_numpy.dot(self.result)%2) == initial)
        for i in range(len(A_numpy.dot(self.result))):
            if (A_numpy.dot(self.result)[i]%2) != initial[i]:
                self.possible = False
        

    def Print_answer(self): #prints the final answer as a set of buttons
        if argv[len(argv)-1] == '-Steps':
            print
            print("""(Note: assigning names to lights in a different order may result in a different (but still correct) answer for the same problem. To find the minimal solution to a general problem and prove it to be minimal, every name permutation would have to be tested)""")
            print
            print("Result: ")
            if(self.possible):
                print("The following lights must be turned off: ")
        answer = list(self.result)
        print_result = ""
        if(self.possible):
            for i in range(len(answer)):
                if answer[i] == 1:
                    print_result = print_result + str(self.nodes[i]) + " "
            print(print_result)
        else:
            print "Impossible"

    def Reset(self): #reverts class variables to initial state
        self.nodes = []
        self.links = [] 
        self.A = []
        self.result = []
        self.possible = True



if __name__ == '__main__':
    L1 = Lights_Puzzle()
    count = 1
    reading = True
    print("Enter input circuit(s) or &Q to exit")
##    print argv[1]
    while(reading == True):
##        for line in stdin.readlines():
        line = stdin.readline()
        if '&Q' == line.rstrip('\n'):
            reading = False
        elif count%2 == 0:
            L1.links = line.strip('\n').split() #fills line of nodes
            count += 1
##           print len(L1.links)
            if argv[len(argv)-1] == '-Steps':
                print("Circuit number %i : " %(count/2))
                print("Lights: " + str(L1.nodes))
                print("Connections: " + str(L1.links))
                print
            if(len(L1.links) != 0):
                L1.Fill_matrix()
                if argv[len(argv)-1] == '-Steps': #shows working if program is run with -Steps
                    L1.Print_state()
                L1.Get_answer()
                L1.Try_answer()
                L1.Print_answer()
            else:
                print_nodes = ""
                if argv[len(argv)-1] == '-Steps':
                    print("No links - answer is to turn off each light separately: ")
                for node in L1.nodes:
                    print_nodes = print_nodes + str(node) + " "
                print print_nodes
            L1.Reset()
            if argv[len(argv)-1] == '-Steps':
                print
                print("-------------------")
                print
        else:
            L1.nodes = line.strip('\n').split() #reads and fills line of links
            count += 1
            
    print("End of Input")
