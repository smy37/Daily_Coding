import sys 

N, M = map(int, sys.stdin.readline().split())
dp = [1 for _ in range(N)]
dp[0] = 1
preq = {i : [] for i in range(1, N+1)}
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    preq[B].append(A)

for i in range(1, N):
    temp = 1
    for k in preq[i+1]:
        temp = max(temp, dp[k-1]+1)
    dp[i] = temp
for i in dp:
    print(i, end=' ')

explain= """
처음에는 접근 방식을 N x N의 배열을 만들고 행을 과목번호, 열을 날짜로 한 후에 날짜별로
선수과목이 이미 수강된 과목을 True로 바꿔주는 것을 생각했다. 그러나 생각해보면 어떤 과목이든 선수과목보다 숫자가 크게 주어지기 때문에
N개의 과목에서 가장 시간이 많이 걸리는 경우 라면 선수과목이 1 -> 2 -> 3 -> 4 -> 5 -> .... -> N 인경우라서 N학기가 걸리는 경우이다.
즉, 과목이 x라고 했을 때, 최대 x일이 걸리고 x일에는 선수과목이 다 이수되어 있는 상태이다. 따라서, 가장 작은 1은 무조건 1학기에 수강이 가능하고
2부터 N 과목에서는 각 과목의 선수과목들 중 가장 오랜 학기가 걸리는 선수과목 소요 학기 + 1 가 소요학기가 된다. 
따라서 [1 for _ in range(N)] 으로 초기화한 dp 배열을 만들고 두번째 부터, N번째 까지 차례대로 선수과목을 살피고(이때, 선수과목은 해당 과목 보다 작기 때문에 다 이수된 상태)
가장 소요학기가 큰 선수과목의 값 + 1을 해줌으로써 dp 배열을 갱신해주면 답을 구할 수 있다.
"""