#Implementation of Hash Tables
# This implementation uses Linked lists to resolve Hash Table Collisions.


class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable():
    def __init__(self, size) -> None:
        self.capacity = size
        self.size = 0
        self.table = [None] * self.capacity
        
    def _hash(self, value):
        return  hash(value) % self.capacity        #The has function is returned and divided by the capacity and the remainder is returned, to be used as our index. This returns a value which is less than the capacity, therefore it is within our list range. i.e 1904 % 10 = 4, it can never be above 10 so it would be within the range 0 - 9

    def insert(self,key, value):
        index = hash(key)            #Here we are using hte inbuilt hash function in python it returns a numeric value based on the key inputted.
        if self.table[index] == None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1


    def delete(self, key):
        for node in self.table:
            current = node
            if key == node.key:
                if current.next:
                    node = current.next
                else:
                    node = None
                self.size -= 1
                return
            else:
                if current.next:
                    while current:
                        if current.next.key == key:
                            current.next = current.next.next
                            self.size -= 1
                            return
                        current = current.next

            raise KeyError(key)             #A key error gets raised if it goes through the function and no match is found


    def search(self, key):
        for node in self.table:
            if node.key == key:
                print(f"Value: {node.value}")
                return
            else:
                current = node.next
                while current:
                    if current.key == key:
                        print(current.next.value)
                        return
                    current = current.next
        raise KeyError(key)     #A key error gets raised if it goes through the function and no match is found

            
    def __len__(self):
        return self.size


    def __contains__(self, key):                #To check if a key is in the Hash table
        try:
            self.search(key)
            return True
        except KeyError:
            return False



class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
  
  
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity
  
    def _hash(self, key):
        return hash(key) % self.capacity
  
    def insert(self, key, value):
        index = self._hash(key)
  
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
  
    def search(self, key):
        index = self._hash(key)
  
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
  
        raise KeyError(key)
  
    def remove(self, key):
        index = self._hash(key)
  
        previous = None
        current = self.table[index]
  
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
  
        raise KeyError(key)
  
    def __len__(self):
        return self.size
  
    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
  
  

  

ht = HashTable(4)

ht.insert("three", 3)
ht.insert("two", 2)
ht.insert("five", 5)

# Checks if the key exists in the hash table: from the __contains__ dunder method
print("three" in ht)  
#Output - True
print("six" in ht)
#Output - False  


print(ht.search("three"))  
# Output - 3


ht.insert("three", 4)
print(ht.search("three")) 
#Output - 4

ht.remove("two")

print(len(ht))  
# Output - 2
    