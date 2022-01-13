import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().strip().split(' ')))
n_dict = {}
for i in n_list:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

n_list = sorted(list(n_dict.keys()))


def binary_search(n, start, end):
    if start == end:
        if n_list[start] == n:
            return True

        else:
            return False

    else:
        mid = (start+end)//2
        if n_list[mid] >= n :
            return binary_search(n, start, mid)
        elif n_list[mid] < n :
            return binary_search(n, mid+1, end)


m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().strip().split(' ')))

start = 0
end = len(n_list)-1
for i in m_list:
    if binary_search(i, start, end):
        print(n_dict[i], end = ' ')
    else:
        print(0, end = ' ')