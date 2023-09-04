import sys

tc_num = int(sys.stdin.readline())

limit = 1000000000000000
for _ in range(tc_num):
    k = int(sys.stdin.readline())
    book = list(map(int, sys.stdin.readline().split()))
    sum_arr = [0 for _ in range(k+1)]
    for i in range(k):
        for j in range(i, k):
            sum_arr[j+1] += book[i]
    dp = [[limit for _ in range(k)] for _ in range(k)]
    for i in range(k):
        dp[i][i] = book[i]
    for i in range(1, k):
        for j in range(k-i):
            for x in range(j, j+i):
                dp[j][j+i] = min(dp[j][j+i], dp[j][x]+dp[x+1][j+i])
            dp[j][j+i] += (sum_arr[j+i+1] - sum_arr[j]) ### 이 부분에서 부분합을 더해주는 아이디어를 기억해두면 좋을듯.
                                                        ## 합치는데 드는 비용과 합쳐져서 만들어지는 수,
                                                        # 이 둘의 합에 다른 값이 붙는다고 생가각하면 불필요한 수의 중복이 일어나지 않는다는것을 알 수 있다.
    print(dp[0][-1]-sum_arr[-1])