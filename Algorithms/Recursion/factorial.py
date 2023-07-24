#Implementation of Factorial Algorithm using two methods



def iterative_factorial(value):
    result = 1
    for i in range(1, value + 1):                   #The loop starts at 1 and ends at the number chosen. Therefore we can multiply from 1 till n .
        result *= i
    return result

print(f"Iteratively calculated: {iterative_factorial(5)}")



def recursive_factorial(value):
    if value == 1:
        return 1
    else:
        return value * recursive_factorial(value - 1)


print(f"Recursively calculated: {recursive_factorial(5)}")