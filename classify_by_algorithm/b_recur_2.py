import sys

cri = int(sys.stdin.readline())

def fivona(n : int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fivona(n-1) + fivona(n-2)

print(fivona(cri))