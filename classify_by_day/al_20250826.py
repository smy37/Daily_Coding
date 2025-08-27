import sys 

N = int(sys.stdin.readline())
dna = sys.stdin.readline().strip()
dp = [[0,0] for _ in range(N)]
if dna[0] == "A":
    dp[0][1] = 1
elif dna[0] == "B":
    dp[0][0] = 1
for i in range(1, N):
    if dna[i] == "A":
        dp[i][0] = min(dp[i-1][0], dp[i-1][1]+1)
        dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1]+1)
    elif dna[i] == "B":
        dp[i][0] = min(dp[i-1][0]+1, dp[i-1][1]+1)
        dp[i][1] = min(dp[i-1][0]+1, dp[i-1][1])

print(dp[-1][0])


explain = """
dp 문제답게 발상자체가 어려웠다. 누적해서 값을 이어가야 하는데 A로 통일할 수 있는 경우와 B로 통일할 수 있는 경우를
지속적으로 기록하는 것을 떠올리는게 쉽지 않았다. 처음에는 A로 통일하는 개수를 누적해서 기록하는 것으로 생각해서 앞에서부터
고려하는 것과 뒤에서부터 고려하는 것 이런 식으로 생각을 전개 하는등 헤맸었다.
"""