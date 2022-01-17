import sys


n = int(sys.stdin.readline())
k = int(sys.stdin.readline())


start = 1
end = n**2


def count(n_num, cri):
    temp = 0
    for i in range(1,n_num+1):
        temp += min(cri//i, n_num)
    return temp

def binary(st, ed):
    if ed - st <=1:

        if count(n, st) >= k:
            return st
        else :
            return ed

    else:
        mid = (st+ed)//2
        tt = count(n, mid)

        if tt>= k:
            return binary(st, mid)
        else:
            return binary(mid+1, ed)


print(binary(start, end))