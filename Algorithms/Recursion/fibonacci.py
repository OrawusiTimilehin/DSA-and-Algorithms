#Implementation of fibonacci sequence using two methods






def iterarive_fibonacci(index):
    n1 = 0
    n2 = 1
    if index == 0 :
        return n1
    elif index == 1 :
        return n2
    else:
        counter = 1
        for i in range(index):
            if counter == index - 1:
                return n1 + n2
            else:
                n3 = n1 + n2
                n1 = n2
                n2 = n3
                counter += 1

print("Iterarive Fibonacci")
print(iterarive_fibonacci(0))
print(iterarive_fibonacci(1))
print(iterarive_fibonacci(9), end='\n\n\n')

def recursive_fibonacci(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    else:
        return recursive_fibonacci(index-1) + recursive_fibonacci(index-2)


print("Recursive Fibonacci")
print(recursive_fibonacci(0))
print(recursive_fibonacci(1))
print(recursive_fibonacci(9))