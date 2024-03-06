import sys

N = int(sys.stdin.readline())

cri = N//5

for i in range(cri,-1,-1):
    t = N-(i*5)
    if t%3 == 0:
        print(i+t//3)
        sys.exit()
print(-1)