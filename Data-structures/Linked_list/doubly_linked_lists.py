# Implementation Doubly Linked lists


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList():
    def __init__(self, ) :
        self.head = None
        self.tail = self.head
        self.size = 0


    def __str__(self) -> dict:
        return self.__dict__()


    def append(self, value) -> str:
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            self.size += 1
        return f"New node ({new_node.data}) has been appended"


    def prepend(self, value) -> str:
        new_node = Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = self.head
            self.size += 1
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
            self.size += 1

        return f"New node ({new_node.data}) has been inserted at position 0"


    def print_list(self, ):
        if self.size == 0:
            print("List is empty\n\n\n") 
        else:
            current = self.head
            while current != None:
                print(f"{current.data, current.next}\n")
                current = current.next
        print( f"The values of the linked list have been printed\n\n\n")
        return 


    def insert(self, position, value) -> str:
        new_node = Node(value)
        if position == 0:
            self.prepend(value)
            return f"Value - {value} has been added to position 0"

        elif position == self.size:
            self.append(value)
            return f"Value - {value} has been appended"
        elif position > self.size:
            print("Position selected is out of range.\n\n")
            return 
        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            new_node.previous = current
            new_node.next = current.next
            current.next.previous = new_node
            current.next = new_node
            self.size += 1

        return f"This Node ({new_node.data} has been inserted at position {position})"


    def delete_by_position(self, position) -> str :
        if position >= self.size:
            print(f"There is no node in that position\n\n")
            return

        elif self.size == 0:
            print(f"The list is empty\n\n")
            return

        elif position == self.size - 1:
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return

        elif position == 0:
            self.head =  self.head.next
            self.head.previous = None
            if self.head == None:
                self.tail = self.head
            self.size -= 1
            return f"The value has been deleted"

        else:
            current = self.head
            for i in range(position - 1):
                current = current.next
            current.next = current.next.next
            current.next.previous = current
            self.size -= 1
            return f"This value has been deleted"


    def delete_by_value(self, value) -> str:
        if self.size == 0:
            return f"Nothing to delete the list is empty"

        current = self.head
        if current.data == value:
            self.head = self.head.next
            if self.head == None:
                self.tail = self.head
            elif self.head != None:
                self.head.previous = None
            self.size -= 1
            return f"This value has been deleted : {value}"

        else:
            current = self.head
            while current.next != None:
                current = current.next
                if current.data == value:
                    if current.next == None:
                        current.previous.next = None
                        self.tail = current.previous
                    else:
                        current.previous.next = current.next
                        current.next.previous = current.previous
                    self.size -= 1
                    return f"This value has been deleted : {value}" 
            print("Given value not found.\n\n\n")               #This only gegts triggered if it goes through the while loop and the value is not found. If it is found the return keyword would have been triggered and the function would have been exited.

        
            
            
        
            
            
my_linked_list = DoublyLinkedList()
my_linked_list.print_list()
#Empty

my_linked_list.append(6)
my_linked_list.append(3)
my_linked_list.append(9)
my_linked_list.print_list()
#6 3 9

my_linked_list.prepend(4)
my_linked_list.print_list()
#4 6 3 9

my_linked_list.insert(2,7)
my_linked_list.print_list()
# 4 6 7 3 9

my_linked_list.insert(0,0)
my_linked_list.print_list()
my_linked_list.insert(6,0)
my_linked_list.print_list()
my_linked_list.insert(9,3)
my_linked_list.print_list()
#This position is not available. Inserting at the end of the list
#Output - 0 4 6 7 3 9 0


my_linked_list.delete_by_value(3)
my_linked_list.print_list()
#Output - 0 4 6 7 9 0

my_linked_list.delete_by_value(0)
my_linked_list.print_list()
#Output - 4 6 7 9 0

my_linked_list.delete_by_position(3)
my_linked_list.print_list()
#Output - 4 6 7 0

my_linked_list.delete_by_position(0)
my_linked_list.print_list()
#Output - 6 7 0

# my_linked_list.delete_by_position(8)
#Out of Range

my_linked_list.delete_by_value(3)
#Given value not found.

print(my_linked_list.size)
#3