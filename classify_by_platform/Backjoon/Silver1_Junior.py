import sys

T = int(sys.stdin.readline())


for _ in range(T):
    answer = 0
    N = int(sys.stdin.readline())
    s = []
    for _ in range(N):
        s.append(list(map(int,sys.stdin.readline().split())))
    s = sorted(s, key = lambda x : x[0], reverse = True)

    cri = N+1

    while s:
        t = s.pop()
        if cri > t[1]:
            answer += 1
            cri = t[1]
    print(answer)