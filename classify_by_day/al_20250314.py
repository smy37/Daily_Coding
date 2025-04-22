import sys

N = int(sys.stdin.readline())

total = []
for _ in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    total.append(temp)

front = {}
back = {}
for i in range(N):
    for j in range(N):
        a1 = total[i][0]+total[j][1]
        if a1 not in front:
            front[a1] = 1
        else:
            front[a1] += 1
answer = 0
for i in range(N):
    for j in range(N):
        temp = total[i][2]+total[j][3]
        if -temp in front:
            answer += front[-temp]
print(answer)


# 6
# -45 22 42 -16
# -41 -27 56 30
# -36 53 -37 77
# -36 30 -75 -46
# 26 -38 -10 62
# -32 -54 -6 45