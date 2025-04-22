import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

num = len(T)

for i in range(num):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[-2::-1]


    if T == S:
        print(1)
        sys.exit()
    if len(T) == 1:
        break

print(0)