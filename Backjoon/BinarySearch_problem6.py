import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

count_list = []
for i in range(1,n+1):
    for j in range(1, n+1):
        count_list.append(i*j)


count_list = sorted(count_list)
print(count_list[k-1])