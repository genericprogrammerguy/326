# Class Node
# Class LinkedList -> Insert, delete, push_front, pop_front, push_back, pop_back
from tkinter import *
# from js2py import *

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.front = None
        self.end = None
        self.length = 0

    def insert_after(self, index, value):
        # if no existing node
        if (self.length == 0):
            node = Node(value)
            self.front = node
            self.length += 1
            self.end = node
        # else add
        elif (self.length - 1 >= index):
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
        if (self.length > 0 and self.length - 1 >= index):
            head = self.front
            for n in range(index):
                head = head.next
            head.next = head.next.next
            self.length -= 1

    def push_front(self, value):
        if self.length == 0:
            self.insert_after(0, value)  # reuse
        else:
            node = Node(value)
            node.next = self.front
            self.front = node
            self.length += 1
            #   to_display=push_front.get()
            #   label_front=Label(window)
            #   label_front["input"]=to_display
            #   label_front.grid(row=12,column=12)
            #   to_display.pack()
            #   print("push")
            #    print(push_value.get())
            #    t1.insert(END, value())

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

    def pop_back(self, value):
        if self.length > 0:
            head = self.front
            for _ in range(self.length - 2):
                head = head.next
            head.next = None
            self.end = head
            self.length -= 1
            #     print("pop")

    # function prints the contents of the linked list
    def print_list(self):
        head = self.front
        while (head is not None):
            #print(head.value, "-> ", end="end")
            head = head.next
        print("NULL")

class DrawLine:
    def __init__(self, window, width, height, colour, row, column):
        self.canvas=Canvas(window, width=width, height=height, bg=colour)
        self.canvas.grid(row=row, column=column)
        self.canvas.bind('<Button-1>', self.draw_line)
        self.canvas.bind('<Button-1>', self.add)
        self.click=0
        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0

    def draw_line(self, event):
        if self.click ==0:
            self.x1=event.x
            self.y1=event.y
            self.click=1
        else:
            self.x2=event.x
            self.y2=event.y
            self.canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill='black', width=10)
            self.click=0

    def add(self, event):
                add = Button(window, width='20', height="3", text="Add", command=insert_after)
                add.grid(row=1, column=0)
                push_value = StringVar()
                add.bind('<Button-1>', ll.insert_after())

                entry_push = Entry(window, textvariable=push_value)
                entry_push.grid(row=1, column=1)

    def pop(self, event):
                pop = Button(window, text="Pop", command=pop_front())
                pop.grid(row=2, column=0)
                #entry_pop = Entry(window)
                #entry_pop.grid(row=2, column=1)

    def push(self, event):
                push_back = Button(window, text="Push", command=push_front())
                push_back.grid(row=3, column=0)
                #entry_pb = Entry(window)
                #entry_pb.grid(row=3, column=1)

# main
if __name__ == '__main__':
    window = Tk()
    window.title("link list Magic")
    draw = DrawLine(window, width=300, height=400, colour='white', row=0, column=0)
    add = draw.add()
    pop = draw.pop()
    push = draw.push()

    window.mainloop()


    # for the Add button
    #  add = Button(window, width='20',height="3", text="Add", command=ll.push_front(1))
    #  add.grid(row=1, column=0)
    #  push_value = StringVar()
    #  entry_push=Entry(window,textvariable=push_value)
    #  entry_push.grid(row=1, column=1)

    #t1 = Text(window, height=1, width=20)
    #t1.grid(row=0, column=2)

    # for the pop button
    #  pop = Button(window, text="Pop", command=ll.pop_back())
    #  pop.grid(row=2, column=0)
    # entry_pop=Entry(window)
    #  entry_pop.grid(row=2, column=1)

    # for the push button
    # push_back = Button(window, text="Push", command=ll.push_back(88))
    # push_back.grid(row=3, column=0)
    # entry_pb=Entry(window)
    # entry_pb.grid(row=3, column=1)

    # window.mainloop()

   # lltest = LinkedList()
   # lltest.push_front(1)
   # lltest.push_front(4)  # 4 -> 1

   # lltest.push_front(3)
   # lltest.push_front(3)
    #lltest.push_front(3)
    #lltest.insert_after(0, 2)
    #lltest.insert_after(0, 5)
    #lltest.print_list()  # 3 -> 5 -> 2 -> 3 -> 3 -> 4 ->1 -> NULL
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
