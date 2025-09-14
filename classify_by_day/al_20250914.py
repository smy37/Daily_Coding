import sys

T = int(sys.stdin.readline())


for _ in range(T):
    N = int(sys.stdin.readline())
    W = int(sys.stdin.readline())
    w_list = list(map(int, sys.stdin.readline().split()))
    p_list = list(map(int, sys.stdin.readline().split()))

    dp = [0]*(W+1)

    for i in range(N):
        w = w_list[i]
        p = p_list[i]
        new_dp = dp[:]
        for j in range(W-w+1):
            new_dp[j+w] = max(new_dp[j+w], p+dp[j])
        dp = new_dp

    print(max(dp))


explain = """
이전에 풀었던 문제와 비슷하다. 현재 물품을 기존에 가능한 모든 무게에 업데이트 해줘야 하므로
이 상황에서 누적되서 업데이트 되지 않도록 새로운 메모리를 만들고 거기에 업데이트 해주고 끝날때
해당 메모리로 기존 메모리를 교체 해줘야 한다.
"""
