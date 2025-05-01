import sys
import math
T = int(sys.stdin.readline())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    num_l = sorted(list(map(int, sys.stdin.readline().split())))

    t_answer = math.inf
    cnt = {}

    for i in range(N-1):
        cur = num_l[i]
        start = i+1
        end = N-1

        while start <= end:
            mid = (start + end) // 2
            temp = cur + num_l[mid]

            t = abs(K-temp)
            if t <= t_answer:
                if t in cnt:
                    cnt[t] +=1
                else:
                    cnt = {t:1}
                t_answer = t

            if temp - K >= 0:
                end = mid-1
            elif temp - K < 0:
                start = mid +1

    for k in cnt:
        print(cnt[k])

## 오늘 푼 문제와 유사하기는 했지만 타겟 K와 가장 유사한 숫자를 찾고 그 숫자를 만드는 조합의 수를 세야 해서 쉽지는 않았다.
## 그리고 숫자의 합이 K보다 큰지 작은지에 따라서 이분탐색의 방향이 결정되는데 막상 K와의 비교를 할 때는 절대값으로 비교해야 되기 때문에
## t라는 값을 가지고 있어야 했고 이 t 값으로 현재의 최근사값을 찾아야 했다. 그러나 오늘 풀었던 이분탐색 문제의 아이디어를 그대로 사용할 수 있었고
## 이분탐색에 대해서 더 많이 풀어봐야 될것 같다.