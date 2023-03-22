# Implementing a Linked List


# Initialisation of the Node class which holds the data and pointer of each element.
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    #Returns the attributes of that node in a dictionary.
    def __str__(self,):
        return f"{self.__dict__}"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # Adds a node to the Linked list
    def append(self, node):
        current = self.head 
        while current.next:
            current = current.next
        current.next = node

    # Removes the last node from the Linked list - It disconnects the link between the second to last and the last node.
    def pop(self,):
        current = self.head             # The current node starts off as the head
        while current.next.next:        # This checks if the nodes next element is pointing to another node. ( If not this means it is the last element so we cut the link to it.)
            current = current.next      # If the next node pointing to another node in sequence it sets the current to the next node.
        current.next = None             # If the next node does not point to any other node it means it is the last node in sequence
                                        # Therefore we set the next of current node to None, which basically cuts the link.
        
    def insert(self, index):
        counter = 0
        current = self.head
        while current:
            if counter < index:
                current = current.next
                

        
        




n1 = Node(5, None)
test = LinkedList(n1)
n2 = Node(10, None)
test.append(n2)
print(n1.next)