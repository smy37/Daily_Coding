import sys

data = int(sys.stdin.readline())

def factorial(n : int):
    if n <=1 :
        return 1
    else:
        return n * factorial(n-1)

print(factorial(data))