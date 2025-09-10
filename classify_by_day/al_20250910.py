import sys

a, d = map(int, sys.stdin.readline().split())

def get_num(k):
    return a+(k-1)*d

def gcd(a, b):
    c = max(a, b)
    d = min(a, b)
    l = c //d
    r = c % d
    if r == 0:
        return l
    return gcd(l, r)

q_num = int(sys.stdin.readline())

for _ in range(q_num):
    q, l, r = map(int, sys.stdin.readline().split())


    if q == 1:
        print((r-l+1)*(get_num(l)+get_num(r))//2)
    elif q == 2:
        if d == 0:
            print(a)
        else:
            a1 = get_num(l)
            print(gcd(a1, d))