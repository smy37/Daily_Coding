import sys 

N = int(sys.stdin.readline())
dp = [["" for _ in range(9)] for _ in range(N+1)]
for i in range(9):
    dp[0][i] = "0"
for i in range(1, N+1):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(1, temp[0]+1):
        cur_n = temp[j]
        for k in range(9):
            if k!= cur_n-1 and len(dp[i-1][k]) > 0:
                dp[i][cur_n-1] = dp[i-1][k]+ str(cur_n)
                break

for t in dp[-1]:
    if len(t) > 0:
        for i in t[1:]:
            print(int(i))
        break
else:
    print(-1)


explain = """
처음 접근 방식은 dfs나 bfs로 탐색 하는 것을 생각했었다. 그런데 N이 <=1000이고 타겟의 종류가 9개라서 9 X N 배열을 만들고 값을 저장해도
될 것 같다는 판단을 하였다. 그리고 가장 핵심이 되는 것은 현재 타겟의 종류를 정할 때는 바로 이전의 경우만 생각해 주면 되고 그 날짜에 해당 타겟을
제공하는 수많은 경우의 수중에 하나만 기록되면 된다는 것이다.
"""