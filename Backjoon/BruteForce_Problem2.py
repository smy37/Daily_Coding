import sys

def findG(n):
    result = n
    for i in str(n):
        result+= int(i)
    return result


def findGenerator(n):
    limit = len(str(n))-1
    boundary = 10**limit-(9*(limit))
    for i in range(boundary, n):
        if findG(i) == n:
            return i
    return 0

temp = int(sys.stdin.readline())
print(findGenerator(temp))