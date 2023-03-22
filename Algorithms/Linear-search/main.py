def unordered_linear_search(value, list):
    for i in list:                                  #Loops through the list until value is located.
        if i == value:
            return f"Found your value: {value} at {list.index(i)}"             # O(n) time complexity.
        


def ordered_linear_search(value, list):
     for i in list:                                  #Loops through the list until value is located.
        if i == value:
            return f"Found your value: {value} at {list.index(i)}"             # O(n) time complexity.
        elif i > value:
            return f"Your value was not found in the array"         # Since it is ordered if the current value is greater than the value we are looking for.....
                                                                    # Then the element does not exist