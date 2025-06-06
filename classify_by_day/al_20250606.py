import sys

T = int(sys.stdin.readline())

for _ in range(T):
    k, N = map(int, sys.stdin.readline().split())

    dp = [0 for _ in range(N + 1)]
    for i in range(k + 1):
        if i <= N:
            dp[i] = 1

    for i in range(1, k):
        new_dp = [0 for _ in range(N+1)]
        for j in range(i+1):
            for l in range(N+1-j):
                new_dp[l+j] += dp[l]
        dp = new_dp

    print(dp[N])

explain = """
처음에 각 테스트 케이스 안에서 for 문을 3번 중첩 안시키기 위해 여러가지로 고민해봤는데 결국 3번 중첩시키는 방법으로 풀게 되었다.
x^N까지의 계수를 dp 배열로 만들어 놓고 처음에 k 범위 안에서 1로 초기화 시킨다 그 후, (1+x)부터 (1+x+x^2)... 순으로 계수들을 업데이트 해주는데
x^0 -> x^1 -> x^2 ... 이런 식으로 x의 승수가 커지게 되면 계수들이 승수만큼 밀려서 업데이트가 된다는 것이 핵심이다. 
"""