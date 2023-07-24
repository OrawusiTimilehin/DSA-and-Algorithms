#Implementation of Bubble Sort

# Time Complexity - O(n^2)
# Space Complexity - O(1) - There is no creation of new memory

def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

numbers = [1, 425, 25, 14, 4, 15, 51, 25, 51, 5]
bubble_sort(numbers)
print(numbers)
