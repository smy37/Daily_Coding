import sys

n = int(sys.stdin.readline())
num_list = sorted(list(map(int, sys.stdin.readline().strip().split(' '))))

m = int(sys.stdin.readline())
cri_list = map(int, sys.stdin.readline().strip().split(' '))

def binary_search(n,start, end):
    if start == end:
        if num_list[start] == n:
            print(1)
            return
        else:
            print(0)
            return

    else:
        mid = (end+start)//2
        if num_list[mid] >= n:

            return binary_search(n, start, mid)
        else:

            return binary_search(n, mid+1, end)

st = 0
en = len(num_list)-1
for i in cri_list:
     binary_search(i, st, en)



