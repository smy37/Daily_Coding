import sys
import math

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


N = int(sys.stdin.readline())

dp = [0]*(N+1)
dp[0] = 1

prime_dict = {}
for i in range(2, N+1):
    if check_prime(i):
        prime_dict[i] = 1


for prime in prime_dict:
    for i in range(N-prime+1):
        dp[i+prime] = (dp[i+prime]+dp[i])%123456789

print(dp[-1])

explain = """
소수를 판별하는 함수를 만들어 놓고 전체 범위에 대해서 소수를 hash로 만들어 놓는다. 
그 후에 소수에 대해서 다이나믹 프로그래밍을 통해서 소수의 합으로 만들어지는 수의 개수를 
누적해서 카운트 해준다.
"""