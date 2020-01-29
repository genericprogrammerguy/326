# Class Node
# Class LinkedList -> Insert, delete, push_front, pop_front, push_back, pop_back
from tkinter import *


class Node:
    def __init__(self, value: object) -> object:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.end = None
        self.length = 0

    def insert_after(self, index, value):
        #if no existing node
        if(self.length == 0):
            node = Node(value)
            self.front = node
            self.length += 1
            self.end = node
        #else add
        elif(self.length - 1 >= index):
            node = Node(value)
            head = self.front
            for _ in range(index):
                head = head.next
            temp = head.next
            head.next = node
            node.next = temp
            if head == self.end:
                self.end = node
            self.length += 1

    def delete_after(self, index):
        if(self.length > 0 and self.length - 1 >= index):
            head = self.front
            for n in range(index):
                head = head.next
            head.next = head.next.next
            self.length -= 1

    def push_front(self, value):
        if self.length == 0:
            self.insert_after(0, value) # reuse
        else:
            node = Node(value)
            node.next = self.front
            self.front = node
            self.length += 1
         #   print("push")
            print(push_value.get())
            t1.insert(END, value())


    def pop_front(self):
        if self.length > 0:
            # temp = self.front
            # temp.next = None
            # del temp # after next line
            self.front = self.front.next
            self.length -= 1

    def push_back(self, value):
        if self.length == 0:
            self.insert_after(0, value)
       #     print("push")
        else:
            node = Node(value)
            self.end.next = node
            self.end = node
            self.length += 1
       #     print("push")

    def pop_back(self):
        if self.length > 0:
            head = self.front
            for _ in range(self.length-2):
                head = head.next
            head.next = None
            self.end = head
            self.length -= 1
       #     print("pop")

    # function prints the contents of the linked list
    def print_list(self):
        head = self.front
        while(head is not None):
            print(head.value, "-> ", end = '')
            head = head.next
        print("NULL")

class Draw:
        def __init__(self, object):
            self.label = Label(object, text="Link List Magic")
            self.label.grid(column=0, row=0)

# main
if __name__ =='__main__':
    window = Tk()
    ll = LinkedList()

    app = Draw(window)

    push = Button(window, text="Add", command=ll.push_front(1))
    push.grid(row=1, column=0)

    push_value = StringVar()
    enter_push=Entry(window,textvariable=push_value)
    enter_push.grid(row=1, column=1)

    t1=Text(window,height=1,width=20)
    t1.grid(row=0,column=2)

 #   pop = Button(window, text="Pop", command=ll.pop_back())
 #   pop.grid(row=2, column=0)
 #   enter_pop=Entry(window)
 #  enter_pop.grid(row=2, column=1)

 #   push_back = Button(window, text="Push", command=ll.push_back(88))
 #   push_back.grid(row=3, column=0)
 #   enter_pb=Entry(window)
 #   enter_pb.grid(row=3, column=1)

    window.mainloop()



   # ll.push_front(1)
   # ll.push_front(4) # 4 -> 1
   # ll.push_front(3)
   # ll.push_front(3)
   # ll.push_front(3)
   # ll.insert_after(0,2)
   # ll.insert_after(0,5)
   # ll.delete_after(0)
   # ll.print_list()
   # ll.delete_after(1)
    # ll.delete(4)
   # ll.print_list() # 3 -> 3 -> 3 -> 4 -> 1 -> NULL |||| # 3 -> 5 -> 2 -> 3 -> 3 -> 4 -> 1 -> NULL
   # ll.push_back(88)
   # ll.print_list()
   # ll.push_front(65)
   # ll.print_list()
   # ll.pop_front()
   # ll.print_list()
   # ll.pop_back()
   # ll.print_list()
   # ll.pop_back()
    # ll.print_list()
