import sys

dna = sys.stdin.readline()
l = len(dna)
dp = [[0]*l for _ in range(l)]


for j in range(1, l):
    for i in range(l-j):
        if (dna[i] == "a" and dna[i+j] == "t") or (dna[i] == "g" and dna[i+j] == "c"):
            dp[i][i+j] = max(dp[i+1][i+j-1] + 2, dp[i][i+j])
        for k in range(i, i+j):
            if dp[i][i+j] < dp[i][k] + dp[k+1][i+j]:
                dp[i][i+j] = dp[i][k] + dp[k+1][i+j]

print(dp[0][l-1])
