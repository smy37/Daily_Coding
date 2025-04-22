import sys
import collections


test_iter = int(sys.stdin.readline())
dp = collections.defaultdict(list)
dp[0] = [1,0]
dp[1] =[0,1]
for i in range(test_iter):
    temp = int(sys.stdin.readline())
    if temp ==1:
        print(0, 1)
    elif temp == 0 :
        print(1, 0)
    elif dp[temp]:
        print(dp[temp][0], dp[temp][1])
    else:
        for j in range(2, temp+1):
            dp[j] = [dp[j-1][0] + dp[j-2][0], dp[j-1][1]+dp[j-2][1]]
        print(dp[temp][0], dp[temp][1])