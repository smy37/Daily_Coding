import sys

N = int(sys.stdin.readline())
if N == 1:
    print(1)
    sys.exit()
accum = 0
tri_l = [accum]
for i in range(1, N):
    accum += i
    temp = tri_l[-1] + accum
    if temp > N:
        break
    tri_l.append(temp)

dp = [N+1]*(N+1)
dp[0] = 0
for i in range(len(tri_l)-1, 0, -1):
    num = tri_l[i]
    for j in range(len(dp)):
        if j+num >= len(dp):
            break
        dp[j+num] = min(dp[j+num], dp[j]+1)

print(dp[-1])