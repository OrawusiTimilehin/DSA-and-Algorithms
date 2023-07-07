# Common Interview Question Merge Sorted Arrays

#Given two arrays that are already sorted combine them into one array which is still sorted.



def merge_sorted_arrays(array1, array2):            #Function takes in two arrays
    array1_index = array2_index = 0                 # We want to keep track of the amount of numbers from each array which has been added to the 
    new_array = []
    
    while array1_index < len(array1) or array2_index < len(array2):         # The loop keeps on running till on of the arrays have been fully used
        if array1[array1_index] <= array2[array2_index]:                    # Checks if the number in the first array is less than or equal to the number in the second array if so it appends to the new array.
            new_array.append(array1[array1_index])                     
            array1_index+=1                                                 #Increments the index counter to keep track of the arrays
        else:
            new_array.append(array2[array2_index])
            array2_index+=1
        
        if array1_index == len(array1):                             #Checks if all the numbers in the array have been appended to the new array
            for num in array2[array2_index:]:                         # If so, then all the remaining numbers in the second array would be appended to the new array as they are already ordered.
                new_array.append(num)                                  
            break                                                   #Breaks out of loop, because the process has been completed.
        
        if array2_index == len(array2):                             #Checks if all the numbers in the array have been appended to the new array
            for num in array1[array1_index:]:                       # If so, then all the remaining numbers in the first array would be appended to the new array as they are already ordered.
                new_array.append(num)
            break                                                    #Breaks out of loop, because the process has been completed.
    return new_array

print(merge_sorted_arrays([1,3,5,7], [2,4,6,8,10,12]))

# Cheat / Pythonic method
# def merge_sorted_arrays(array1, array2):
#     array1.extend(array2)
#     print(array1)
#     array1.sort()
#     return array1
 




