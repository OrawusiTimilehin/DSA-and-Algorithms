###Implementing an array

##Time Complextiy of operations

# Lookup/Access - O(1)
# Append - O(1) - Although can sometimes be O(n) in the case of dynamic arrays you can add as much values as you want but from the low level point of view the computer allocates a block of adjacent memory addresses for your array 
# and although we can keep on adding under the hood when that block of memory get full the computer has to find another free space usually doubles the size, copies the array now and where the array and puts it there where you can keep on adding until its full again and the process continues.
#  That's why sometimes it can be O(n). 
# Insert - O(n)
# Search - O(n)
#

class Array:
    def __init__(self,):
        self.length = 0  # The length of the array 
        self.data = {}   # The data of the array is to be stored in the dictionary with its keys corresponding to its index.

    # Returns the attributes of the Array in a dictionary.
    def __str__(self,):
        return f"{self.__dict__}"

    # Returns the element of that specified index
    def get(self, index):
        return self.data[index]

    # Adds an element to the end of the Array
    def push(self, value):
        self.data[self.length] = value    
        self.length += 1
        return self.data                    # O(1) - Operation

    # Removes an element from the end of the Array
    def pop(self,):
        if self.length > 0 :        #Checks if the array is empty or not 
            value = self.data[self.length -1]  # Holds the  element  to be removed
            del self.data[self.length -1]      # Removes the value from the end of the Array 
            self.length -= 1                    # Reduces the length of the array
        return value                        # Returns the element which was removed
                                            # O(1) - Operation


    # Inserts a value at a specific index

    def insert(self, item, index):
        for i in range(self.length, index, -1):     # Loops backwards from the end of the list to the index specified
            self.data[i] = self.data[i-1]              # Shifts every element one place to the right.
        self.data[index] = item                         # Replaces the value at that given index with the value specified.
        return self.data                                # O(n) Operation

    # def insert(self, value, index):
    #     for i in range(self.length, index, -1):        # Loops backwards from the end of the list to theindex specified
    #         self.data[i] = self.data[i - 1]            # Shifts every element one place to the right.
    #     self.data[index] = value                       # Replaces the value at that given index with the value specified.
    #     return self.data                               # O(n) Operation
    
    # Removes a value at a specified index
    def delete(self, index):
        if index >= self.length:            # Checks if the index specified is above the array
            return f"Index is outsied of range"
        else:
            for i in range(index, self.length):
                self.data[i] = self.data[i + 1]            # Shifts every element to the left by replacing each element with the one after it.
            del self.data[self.length]                     # Deletes the last element at the last index which we do not need anymore.
            return self.data                               # O(n) Operation            

test = Array()

# test.push(1)
# test.push(2)
# test.push(4)
# test.push(5)
# test.get(1)
# test.pop()
# print(test.insert(3, 2))
# print(test.__str__())
# print(test.delete(4))


# print(test.__str__())

    











