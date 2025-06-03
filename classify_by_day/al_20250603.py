import sys 

N = int(sys.stdin.readline())
dp = [i for i in range(N+1)]

### 1. First Method
for i in range(N+1):
    for j in range(i+3, N+1):
        dp[j] = max(dp[j], dp[i]*(j-i-1))
print(dp[-1])


### 2. Second Method
# for i in range(5, N+1):
#     dp[i] = max(dp[i], dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
# print(dp[-1])

explain = """
대부분의 dp 문제가 그러하듯, 점화식을 떠올리면 구현은 쉬운 문제이다.
그러나 해당 점화식을 떠올리는게 쉽지 않았다. 특히 두번째 방법의 점화식은
증명하는 부분에 대해서 좀 더 고민을 해봐야 할 것 같다. 
첫번째 방식처럼 복사에 대해서만 생각하고 dp 메모리를 갱신해 주면 이유에 대해 생각해보면
얼핏 생각하면 선택 복사 붙혀넣기 후, 그냥 A를 출력하는 1번 명령어를 중간에 섞어주고 다시 
선택 복사 붙혀넣기 하는 것이 가능하다고 생각하지만 무조건 6이상 부터는 
이전의 값을 복사해서 해당 수에 도달하는 것이 같으 명령어 수 내에서 최대 값을 얻을 수 있다는 것을 
명심해야 한다.
"""