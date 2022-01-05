import sys

target = int(sys.stdin.readline())

def decompose(n : int):
    length = len(str(n))
    temp = n
    run = n
    for i in range(length):
        temp += run % (10)
        run = run // (10)

    return temp

temp = 10**(len(str(target))-1) - 9*(len(str(target))-1)

for i in range(temp, target):
    if decompose(i) == target:
        print(i)
        sys.exit()

print(0)