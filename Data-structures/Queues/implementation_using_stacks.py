
#Implementation using arrays - note: but never use an array to implement a stack because it is less efficient than using a Linked List because of the O(n) operations when you dequeue.
# class Queue():
#     def __init__(self) -> None:
#         self.array = {}
#         self.size = 0

#     def peek(self):
#         print(self.array[0])
#         return

#     def enqueue(self, value):
#         self.array[self.size] = value
#         self.size += 1
#         return

#     def dequeue(self):
#         for i in range(self.size - 1):
#             self.array[i] = self.array[i + 1]
#             self.size -= 1
#             return

#     def print_queue(self):
#         for key, value in self.array.items():
#             print(f"{key, value}")
#         return


    