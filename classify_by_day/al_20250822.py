import sys

T = int(sys.stdin.readline())
cri = 1000000007

### 1. First Method
# n_list = []
#
# for _ in range(T):
#     n = int(sys.stdin.readline())
#     n_list.append(n)
#
# max_n = max(n_list)
# dp = [0]*(max_n+1)
# dp[1] = 1
#
# for i in range(1, max_n+1):
#     for j in range(i+1, max_n+1):
#         dp[j] = (dp[j] + dp[i]%cri)%cri
#
# for n in n_list:
#     print(dp[n])

### 2. Second Method
for _ in range(T):
    n = int(sys.stdin.readline())
    if n <= 2:
        print(1)
    else:
        print(pow(2, n-2, cri))


explain = """
첫번째 시도에서는 dynamic programming을 이용해서 풀려고 했지만 메모리 초과가 발생하였다.
그런데 점화식을 살펴보면 A_n+1 = 2*A_n과 같다. 왜냐하면 n+1번째 원소는 n번째 원소까지의 합인데
n번째 원소가 n-1번째 원소까지의 합과 같아서 2*(n번째 원소의 값)이 n+1번째 원소의 값이 된다.
"""