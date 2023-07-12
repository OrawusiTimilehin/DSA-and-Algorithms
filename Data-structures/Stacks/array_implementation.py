# # Implementation of a Stack 

# # This is a linear data structure which operates on the principle LIFO. 

# # Stacks are used in use cases for
# #  Browser history 
# # Undo and version control in a word processor
# # Function calling in some programming languages (Call Stack)


# # Operations 
# # Lookup - O(n)
# # Push - O(1)
# # Pop - O(1)
# # Peek - O(1)


# So for a stack we push and pop from one end which is usually the end of the stack. So if we use an array appending and popping have time complexities of O(1) this is also the case of a linked list where the end of the stack can be the front of the linked list and you can just prepend or remove the head which is still an O (1). 

# Now the reason to choose either, is memory, array values are stored in contiguous memory this means accessing data in the data structure maybe faster than in a linked list and pointers in a linked list take more memory. But Linked lists have more dynamic memory where you can keep on adding items while arrays have a point where they reach their limit and you have to double up that memory and create a new space for it. So depends on what operations you are doing and what your priorities are. 




class Node():                   #Linked lists are made using nodes so we would need a node class
    def __init__(self, value = None, next = None):
        self.data = value
        self.next = next


class Stack():
    def __init__(self) -> None:
        self.array = []

    def push(self, value):              #Appends the value to the end of the stack which is the top of the stack for this implementation
        self.array.append(value)


    def pop(self):                              #Removes a value from the top pf the stack list 
        if len(self.array) == 0:
            print("Stack is empty")
        else:
            self.array.pop()            # The pop is an in-built function by python with a time complexity of O(1)


    def peek(self, ):                                #Returns the top value of the stack
        return self.array[len(self.array) - 1]

    def display_stack(self,):
        print(self.array)




my_stack = Stack()
my_stack.push(10)
my_stack.push(209)
my_stack.push(1042)
my_stack.push(429)
my_stack.display_stack()

#Output - 10, 209, 1042, 429


my_stack.pop()
my_stack.pop()
my_stack.display_stack()

#Output - 10, 209


print(my_stack.peek()) 
#Output - 209



