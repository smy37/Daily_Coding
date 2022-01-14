import sys

############# 처음에 시도했던 방법으로 정리해보기........

k, n = map(int, sys.stdin.readline().strip().split(' '))

line_list = []
for i in range(k):
    line_list.append(int(sys.stdin.readline()))

end = max(line_list)
start = 1

def cnt_temp(n_list, i):
    temp_c = 0
    for j in n_list:
        temp_c += j//i
    return temp_c

def binary_search(n_list, start, end):
    mid = (start+end)//2
    if start == mid:
        if cnt_temp(n_list, end) == n:
            return end
        else:
            return start

    else:
        temp = cnt_temp(n_list, mid)

        if n > temp:
            return binary_search(n_list, start,mid)
        elif n <= temp:
            return binary_search(n_list, mid, end)


print(binary_search(line_list, start, end))