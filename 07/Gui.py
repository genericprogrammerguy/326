# Class Node
# Class LinkedList -> Insert, delete, push_front, pop_front, push_back, pop_back


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
        if(self.length == 0):
            node = Node(value)
            self.front = node
            self.length += 1
        elif(self.length - 1 >= index):
            node = Node(value)
            head = self.front
            for n in range(index):
                head = head.next
                temp = head.next
                head.next = node
                node.next = temp

    def delete(self, index):
        if(self.length > 0 and self.length - 1 >= index):
            head = self.front
            for n in range(index):
                head.next = temp

    def push_front(self, value):
        node = Node(value)
        node.next = self.front
        self.front = node
        self.length += 1

    def pop_front(self):
        pass

    def push_back(self):
        pass

    def pop_back(self):
        pass

    # function prints the contents of the linked list
    def print_list(self):
        head = self.front
        while(head is not None):
            print(head.value, "-> ", end = '')
            head = head.next
        print("NULL")


# main
if __name__ =='__main__':
    ll = LinkedList()
    ll.push_front(1)
    ll.push_front(4) # 4 -> 1
    ll.insert_after(0, 2)
    ll.print_list()
    ll.insert_after(0, 5)
    ll.print_list()
