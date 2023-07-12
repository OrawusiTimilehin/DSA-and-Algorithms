# Implementation of a Stack 

# This is a linear data structure which operates on the principle LIFO. 

# Stacks are used in use cases for
#  Browser history 
# Undo and version control in a word processor
# Function calling in some programming languages (Call Stack)


# Operations 
# Lookup - O(n)
# Push - O(1)
# Pop - O(1)
# Peek - O(1)


# So for a stack we push and pop from one end which is usually the end of the stack. So if we use an array appending and popping have time complexities of O(1) this is also the case of a linked list where the end of the stack can be the front of the linked list and you can just prepend or remove the head which is still an O (1). 

# Now the reason to choose either, is memory, array values are stored in contiguous memory this means accessing data in the data structure maybe faster than in a linked list and pointers in a linked list take more memory. But Linked lists have more dynamic memory where you can keep on adding items while arrays have a point where they reach their limit and you have to double up that memory and create a new space for it. So depends on what operations you are doing and what your priorities are. 




class Node():                   #Linked lists are made using nodes so we would need a node class
    def __init__(self, value = None, next = None):
        self.data = value
        self.next = next



class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.size = 0

    def push(self, value ) -> str:              #Pushes a value to the back of the linked list an append operation which is an O(1) operation
        new_node = Node(value)
        if self.size == 0:
            self.top = new_node
            self.bottom = self.top
            self.size += 1
        else:
            new_node.next = self.top
            self.top = new_node
            self.size += 1

    def pop(self, ) -> str:                         #Removes a value from the list from the top of the linked list
        if self.size == 0:
            print("List is empty nothing to Pop")
        else:
            self.top = self.top.next
            if self.top == None or self.top.next == None:
                self.tail = self.head
            self.size -= 1
            


    def peek(self, list) -> str:                #Returns the top value of the list which is the head of the linked list
        top_value = self.top
        return f"The top value is {top_value}"


    def display_stack(self, ) -> list:                   #This method displays the list and all its data. It traverses through the list and appends all the data to a list which is returned byt hte function
        if self.size == 0:
            return "The list is empty"
        else:
            current = self.top
            array = []
            while current:                                              #Loops through the list and if the current node is not None then it appends the data of the node to the list.
                array.append((current.data, current.next))
                current = current.next
            return array



my_stack = Stack()

my_stack.push(9)
my_stack.push(8)
my_stack.push(10)
my_stack.push(11)
my_stack.push(900)

print(my_stack.display_stack(), end='\n\n\n')
#Output -  900 11 10 8 9


my_stack.pop()
print(my_stack.display_stack(), end='\n\n\n')
#Output - 11 10 8 9      - In reverse because the stack appends to the front 




