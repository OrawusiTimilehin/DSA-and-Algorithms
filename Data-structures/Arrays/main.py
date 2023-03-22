#Implementing an array

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
        if self.length > 0 :
            value = self.data[self.length]  # Holds the  element  to be removed
            del self.data[self.length]      # Removes the value from the end of the Array 
        return value                        # Returns the element which was removed
                                            # O(1) - Operation


    # Inserts a value at a specific index
    def insert(self, value, index):
        for i in range(self.length, index, -1):        # Loops backwards from the end of the list to theindex specified
            self.data[i] = self.data[i - 1]            # Shifts every element one place to the right.
        self.data[index] = value                       # Replaces the value at that given index with the value specified.
        return self.data                               # O(n) Operation
    
    # Removes a value at a specified index
    def delete(self, index):
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
# print(test.delete(4))


print(test.__dict__)

    


