#Implementation of a Queue using a Llinked List



class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
class Queue():
    def __init__(self, ) -> None:
        self.front = None
        self.back = None
        self.size = 0

    def peek(self, ):
        print(f"The first item in the queue is {self.front}\n\n\n")
        return self.front

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.front = new_node
            self.back = self.front
            self.size += 1
        else:
            self.back.next = new_node
            self.back = new_node
            self.size += 1

        return f"Value:{value} added"

        

    def dequeue(self, ):
        if self.size == 0:
            print("The List is empty nothing to dequeue\n\n\n")
        else:
            self.front = self.front.next
            if self.front == None:
                self.back = self.front
            self.size -= 1 

    def print_queue(self, ):
        if self.size == 0:
            print("Queue is empty\n\n\n")
            return
        else:
            current = self.front
            while current != None:
                if current.next == None:
                    print(f"{current.data, current.next}")
                else:
                    print(f"{current.data, current.next}  <<---", end=' ')
                current = current.next
            return 



my_queue = Queue()
my_queue.enqueue("My")
my_queue.enqueue("name")
my_queue.enqueue("is")
my_queue.enqueue("Timi")
my_queue.print_queue()
#My  <<---  name  <<---  is  <<---  Timi

print(my_queue.peek())
#My

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#is  <<---  Timi

print(my_queue.__dict__)
#{'front': <__main__.Node object at 0x1012e0d90>, 'back': <__main__.Node object at 0x1012e0dd0>, 'size': 2}
print(my_queue.front)
#<__main__.Node object at 0x1012e0d90>
print(my_queue.front.data)
#is

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
#Queue is empty