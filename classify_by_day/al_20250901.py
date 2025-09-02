import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

for i in range(num_list[1], 0, -1):
    cri = num_list[0]%i
    for j in range(1, len(num_list)):
        if cri != num_list[j]%i:
            break
    else:
        print(i)
        break