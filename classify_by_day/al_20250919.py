import sys 

num = sys.stdin.readline().strip()


dp = [[0, 0] for _ in range(len(num))]
dp[0][0] = 1

for i in range(1, len(num)):
    pre_n = int(num[i])

    if pre_n > 0:
        dp[i][0] = sum(dp[i-1])
    
    pre_pre_n = int(num[i-1:i+1])

    if 10<=pre_pre_n<=34:
        dp[i][1] = dp[i-1][0]

print(sum(dp[-1]))

explain = """
현재 자리의 숫자가 일의 자리일 경우에는 이전 단계에서 일의 자리와 십의 자리 숫자의 합으로
현재 자리의 숫자가 십의 자리일 경웬느 이전 단계에서 일의 자리일 경우의 개수가 된다. 
가능한 카드가 1~34 임을 유의한다.
"""