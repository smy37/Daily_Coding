import sys

N, M = map(int, sys.stdin.readline().split())

sum_t = [0 for _ in range(N)]
t = list(map(int, sys.stdin.readline().split()))
cnt = 0
sum_t[0] = t[0]
div_t = {i : 0 for i in range(M)}
div_t[sum_t[0]%M] += 1
for i in range(1,N):
    sum_t[i] += sum_t[i-1] + t[i]
    div_t[sum_t[i] % M] += 1

cnt += div_t[0]

for k in div_t:
    t = div_t[k]
    cnt += int((t-1)*t/2)


print(cnt)