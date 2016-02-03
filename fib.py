#!/usr/bin/python
# 0 1 1 2 3 5 8 13 21 ...

def fib(n):
    return fib_rec([], 0, n)

# recursive fibonacci
def fib_rec(arr, index, n):
    if len(arr) > 0 and arr[-1] >= n:
        if arr[-1]>n:
            arr.pop()
        return arr
    elif index == 0:
        arr.append(0)
    if index == 1:
        arr.append(1)
    if index > 1 < n:
        arr.append(arr[index-1] + arr[index-2])
    return fib_rec(arr, index+1, n)

# iterative fibonacci
def fib_iter(n):
    arr = [0, 1]
    index = 1
    aux = 0
    while aux < n:
        aux = arr[index-1] + arr[index]
        arr.append(aux)
        index = index + 1
    if arr[-1] > n:
        arr.pop()
    return arr

print "Recursive fibonacci: " + str(fib(22))
print "Iterative fibonacci: " + str(fib_iter(22))

