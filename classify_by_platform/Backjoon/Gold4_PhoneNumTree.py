import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    p_l = []
    for i in range(N):
        t = sys.stdin.readline().strip()
        p_l.append(t)
    p_l = sorted(p_l)
    flag = True
    for i in range(1, len(p_l)):
        cri = len(p_l[i-1])
        if p_l[i][:cri] == p_l[i-1]:
            print('NO')
            flag = False
        if not flag:
            break
    if flag:
        print('YES')