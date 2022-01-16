import sys

h, g = map(int, sys.stdin.readline().strip().split(' '))

h_list = []
for i in range(h):
    h_list.append(int(sys.stdin.readline()))
h_list = sorted(h_list)


def check(houselist, d):
    cur = houselist[0]
    cnt = 1

    for i in range(1, len(houselist)):
        if houselist[i]- cur >= d:
            cur = houselist[i]
            cnt +=1

    return cnt

start = 1
end = h_list[-1]-h_list[0]
def binary(st, ed):
    if ed - st <=1 :
        if check(h_list, ed) >= g:
            return ed
        else:
            return st
    else:
        mid = (st+ed)//2
        temp = check(h_list, mid)

        if temp>= g:
            return binary(mid, ed)
        else:
            return binary(st, mid-1)

print(binary(start, end))
