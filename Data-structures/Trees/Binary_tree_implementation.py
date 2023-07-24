# Implementation of a Binary Tree

class Node():
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None
        self.num_of_nodes = 0


    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            self.num_of_nodes += 1
            return
        else:
            current = self.root
            while current != None :
                print(current.data, end="\n\n\n")
                if value < current.data:
                    current = current.left_child
                    print(current.data, end="\n\n\n")
                elif value >= current.data:
                    current = current.right_child
                    
            current = new_node
            print(current.data, end="\n\n\n")
            print(self.root.right_child)
            self.num_of_nodes += 1
            return
            
    def search(self, value):
        if self.root == None:
            print("Tree is empty\n\n\n")
            return

        current = self.root
        while current != None:
            print("Started the while loop")
            if current.data == value:
                print(f"Found value: {value} in the tree\n\n\n")
                return
            else:
                print("Entered the else block")
                if value < current.data:
                    current = current.left_child
                elif value > current.data:
                    print("Entered the elif block")
                    current = current.right_child
                    # print(current.data)
        print("Value not found.")               #Gets triggered only if the value is not found. If it was found the function would have been exited.

    # def delete(self, value):
    #     current = self.root
    #     while current = 

    

my_bst = BinarySearchTree()
# my_bst.insert(5)
# my_bst.insert(3)
# my_bst.insert(7)
# my_bst.insert(1)
my_bst.insert(13)
my_bst.insert(65)
# my_bst.insert(0)
# my_bst.insert(10)


# my_bst.search(13)
# my_bst.search(65)
# my_bst.search(0)
# my_bst.search(10)

