import sys 

D, K = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(D+1)]
dp[2] = 1

for i in range(3, D+1):
    dp[i] = dp[i-1] + dp[i-2]

cri_a = dp[D-1]
cri_b = dp[D]

for i in range(K//cri_b, 0, -1):
    if (K-(cri_b*i))%cri_a == 0 and K!= cri_b*i:
        print((K-(cri_b*i))//cri_a)
        print(i)
        break


explain = """
dp를 이용해서 미지수의 계수를 저장한 후, 브루트 포스로 해당 계수에 미지수들을 대입해서 답을 구하는 문제.
dp에서 B의 계수를 쌓았을 때, B의 계수 하나 이전이 A의 계수가 된다는 점을 이용하면 된다. 
브루트 포스를 통해서 계수가 주어질 때, 미지수를 구했지만 속도가 좀 더 빡빡했다면 이진 탐색을 시도해봐도 좋을 것 같다.
하나 주의할 점은, (K-(cri_b*i)) 부분에서 K=cri_b*i 가 되는 상황인데 이렇게 되면 첫날 준 떡의 개수가 0이 되므로 예외 처리를 해줘야 한다.
"""