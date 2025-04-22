import sys

iter_num = int(sys.stdin.readline())

tri = []
for i in range(iter_num):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    tri.append(temp)

tri = tri[-1::-1]
cri = len(tri)-1

for i in range(cri):
    for j in range(cri-i):
        tri[i+1][j] += max(tri[i][j], tri[i][j+1])

print(tri[-1][0])