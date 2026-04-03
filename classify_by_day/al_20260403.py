import sys 

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))



answer = 0
for i in range(N):
    idx = i
    cur = 0
    while 1:
        cur += num_list[idx]
        if cur == 50:
            answer += 1
            break
        elif cur > 50:
            break
        idx += 1
        if idx >= N:
            idx -= N

print(answer//2)