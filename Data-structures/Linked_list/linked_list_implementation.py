# # Implementing a Linked List

## Time Complexity of Operations
#Append - O(1)
#Prepend - O(1)
#Insert - O(n)
#Delete - O(n)
#Lookup - O(n)

class Node():                                   #The Node class would act as a block which holds the value and the pointer to the next node in the list
    def __init__(self,data, next=None ):
        self.data = data
        self.next = next
        
    

class LinkedList():
    def __init__(self,):
        self.head = None                    #The head is instantiated as None because the list is empty 
        self.tail = self.head               #The tail points to the head at instantiation because the list is empty and the tail is the head.
        self.size = 0                       #Holds the size of the list 
    
    def append(self, value):                #This method adds a node to the end of the list 
        new_node = Node(value)              #Creation of a Node from the Node class
        if self.head == None:                  #If the list is empty it sets the head to be the new node created and the tail to be the same
            self.head = new_node            
            self.tail = self.head
            self.size = 1                       #Sets the size to be 1 as the list contains only 1 node
        else:
            self.tail.next = new_node           #If the list is not empty then the next of the tail becomes the new node and the new_node becomes the tail
            self.tail = new_node
            self.size +=1                       #Increments the size of the list


    def prepend(self, value):       #This method adds a node to the front of the list
        new_node = Node(value)                  
        if self.head == None:               #If the list is empty the head becomes the new node and the tail becomes the head.
            self.head = new_node    
            self.tail = self.head
            self.size = 1
        else:
            new_node.next = self.head               #The next of the new node becomes the current head 
            self.head = new_node                    #The head becomes the new node
            self.size += 1


    def display_list(self, ) -> list:                   #This method displays the list and all its data. It traverses through the list and appends all the data to a list which is returned byt hte function
        if self.size == 0:
            return "The list is empty"
        else:
            current = self.head
            linked_list = []
            while current:                                              #Loops through the list and if the current node is not None then it appends the data of the node to the list.
                linked_list.append((current.data, current.next))
                current = current.next
            return linked_list



    def insert(self, position , value):                     #Method to insert a value at any position
        new_node = Node(value)
        if self.size == 0 :                                 #This block handles the case where the list is empty, same as appending to an empty list
            self.head = new_node
            self.tail = self.head
            self.size += 1

        elif position > self.size:                              #Checks if the index or position selected is within the range
            print( f"Index is out of range", end='\n\n\n')

        elif position == 0:                             #Caters to case where the insert is in the position 0, basically a prepend operation
            new_node.next = self.head
            self.head = new_node
            self.size += 1

        elif position == self.size:                    #If the position is equal to the size then it is an append function, because it is inserting at the back 
            self.tail.next = new_node
            self.tail = new_node                        #This ensures that the tail is reset to the new node
            self.size += 1
        else:
            current = self.head                     #Block of code that deals with inserting in the middle or between nodes
            for i in range(position - 1 ):           # This loops up until the node before the position we want to insert a new node in. It then makes that current node's next the next of the node we are currently inserting and the next of the new node would be the next of the current node this way it links the current node to the new node and the new node to the next node. Hope it makes sense 😂
                current = current.next
            new_node.next = current.next            
            current.next = new_node
            self.size += 1
            

    def delete_by_position(self, position):                     # This method allows us to delete a node by its position
        if self.size == 0 or position > self.size:              # Checks if the list is empty or the position is out of the range of the list.
            print( "The position is out of range", end='\n\n\n')
        elif position == 0 :                            # If the position that the node is to be inserted in is 0 which is the head position then the head becomes the previous head's next. Also the size is incremented by 1
            self.head = self.head.next
            if  self.head == None:           # Checks for the case where there are two nodes in the list or one node in the list in each case the tail woudl be the same as the head. Which is either none or the only node in the list.
                self.tail = self.head    
            self.size -= 1
        else:
            current = self.head
            for i in range(position - 1):          # This loops up until the node before the node we want to delete, it then makes that current node's next the next of the node we are currently deleting this way it links the previous and next node of the node we want to delete. Hope it makes sense 😂
                current = current.next
            current.next = current.next.next
            self.size -= 1
            if current.next == None:        #If the current node's next is none that means we jsut deleted the last node and are currnetly on the new tail which should be adjusted accordingly.
                self.tail = current 
            
        
    def delete_by_value(self, value):        # This method allows us to delete a node by its value, it traverses the list until it finds the node with the value and deletes it.
        if self.size == 0:                    # Checkcs if the list is empty, if so nothing to delete
            return "The list is empty, nothing to delete"

        current = self.head

        if current.data == value:                       # The current node is the head, if the current node has the value we are looking for there is no need to loop through, we just make the head node's next the new head.
            self.head = self.head.next
            if current == None or current.next == None:             # Checks for the case where there are two nodes in the list or one node in the list in each case the tail woudl be the same as the head. Which is either none or the only node in the list.
                self.tail = self.head    
            self.size -= 1
            return f"Deleted this value - {current.data}"               #For this particular case the Time Complexity is O(1)

        while current:                          #This loops through the list and checks if the nodes next's value is equal to the data if so it cuts the link and relinks with the node after the node we are currently deleting.
            if current.next.data == value:
                current.next = current.next.next
                self.size -= 1
                if current.next == None:
                    self.tail = current
                return f"Deleted this value - {current.data}"       
            current = current.next

        if current == None:
            return f"This value does not exist in the list"

        
        


        
if __name__ == "__main__":              #This file is going to be imported into other files so inorder for it not to run these commands this is used
    my_linked_list = LinkedList()
    print(my_linked_list.display_list(), end='\n\n\n')

    #Output - Empty

    my_linked_list.append(5)
    my_linked_list.append(3)
    my_linked_list.append(10)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output - 5 3 10

    my_linked_list.prepend(4)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output - 4 5 3 10


    my_linked_list.insert(2,7)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output - 4 5 7 3 10

    my_linked_list.insert(0,0)
    my_linked_list.insert(6,0)
    my_linked_list.insert(9,3)
    print(my_linked_list.display_list(), end='\n\n\n')

    #Output - 0 4 5 7 3 10 0

    my_linked_list.delete_by_value(3)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output - 0 4 5 7 10 0

    my_linked_list.delete_by_value(0)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output -  4 5 7 10 0


    my_linked_list.delete_by_position(3)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output -  4 5 7 0


    my_linked_list.delete_by_position(0)
    print(my_linked_list.display_list(), end='\n\n\n')
    #Output -  5 7 0


    my_linked_list.delete_by_position(8)
    #Output -  Out of Range 


    print(my_linked_list.size, end='\n\n\n')
    #Output - 3