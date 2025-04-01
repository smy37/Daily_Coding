def GetMaxScore(scores):
    # Write your code here
    answer = 0
    n = len(scores)
    dp = [[0 for i in range(n)], [0 for i in range(n)]]
    if n == 1:
        answer = max(0,scores[0])
    dp[0][0] = scores[0]    ## Not Skip
    dp[1][0] = 0            ## Skip

    for i in range(1, n):
        for j in range(2):
            if j == 0:  ## Not Skip
                dp[0][i] = max(dp[0][i-1]+scores[i], dp[1][i-1]+scores[i])
            elif j == 1:    ## Skip
                dp[1][i] = dp[0][i-1]

    answer = max(dp[0][n-1], dp[1][n-1])
    return answer

print(GetMaxScore([9, -1, -3, 4, 5]))