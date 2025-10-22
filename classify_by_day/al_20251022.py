import sys 

N = int(sys.stdin.readline())
dp = [float("inf") for _ in range(N+1)]
dp[0] = 0

upper_bound = int(N**0.5)

for i in range(upper_bound, 0, -1):
    pow_i = i*i
    for j in range(N-pow_i+1):
        dp[j+pow_i] = min(dp[j+pow_i], dp[j]+1)

print(dp[-1])

explain = """"
동전 문제와 유사하게 제곱근을 통해 넣을 수 있는 가장큰 제곱수를 구한다. 
그리고 가장 큰수부터 메모리를 업데이트 해준다.
"""