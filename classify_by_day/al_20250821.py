import sys

cri = 1000000000
dp = [0, 1]
while 1:
    temp = dp[-1] + dp[-2]
    if temp > cri:
        break
    dp.append(temp)

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
