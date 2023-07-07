# Common Interview Question - Reverse a String


def reverse(word):
    word_list = []
    for i in range(len(word) - 1, -1, -1):  #Loops through each letter  of the word from the back.
        word_list.append(word[i])           #Adds each of the letters to a list
    new_word = ''.join(word_list)          #Joins all the elements of the list
    return new_word


print(reverse("My name is Oluwatimilehin"))

#Now this is the simpler way of reversing a string, which has a Time Compleity of O(n) 
# This is because it loops through every letter in the word (goes through all the input)
# It also has a space complexity of O(n) because it appends to the list for each letter, we are creating a new item in memory each input.


#There is a smarter way of reversing a string which saves us space and makes the space complexity O(1).
# In this method we swap letters from both ends of the word until we reach the middle this ends up reversing the string, 
# this way we do not need to create a new array which would take up space in memory.


def swap(string, a, b):        #This is the function to swap to letters
    string = list(string)       #Converts String to a list because strings do not support item assignment it is immutable 
    temp = string[b]
    string[b] = string[a]       #Switches letters
    string[a] = temp    
    return ''.join(string)      #Joins list to form a string


def reverse(string):
    for i in range(len(string)//2):                 #Only loops half of the length of the string because the switch happens in pairs
        string = swap(string, i, len(string)-i-1)       
    return string


print(reverse("My name is Oluwatimilehin"))

#Time Complexity still remains at O(n)