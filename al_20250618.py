import sys 

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())

    dp = [0]*(M+1)
    dp[0] = 1
    for n in coins:
        if n > M:
            continue
        for i in range(M-n+1):
            dp[i+n] += dp[i]
            
    print(dp[-1])

explain = """
Dynamic Programming의 전형적인 문제, 
현재 위치에서 저장하고 있는 값을 다음 스텝으로 이동한 값에 더해주는것이 포인트.
"""