import sys

def check_divide(a, b):
    for i in range(2, a+1):
        if a%i == 0 and b%i == 0:
            return False
    return True

X, Y = map(int, sys.stdin.readline().split())

vic_l = []
defeat_l = []
for i in range(X, Y):
    if check_divide(i, Y):
        defeat_l.append(i)
    else:
        vic_l.append(i)

print(defeat_l)
print(vic_l)
