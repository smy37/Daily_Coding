import sys
import math

N, M = map(int , sys.stdin.readline().split())

min_six_p, min_one_p = float("inf"), float("inf")
for _ in range(M):
    six_p, one_p = map(int, sys.stdin.readline().split())

    if 6*one_p < six_p:
        min_six_p = min(min_six_p, 6*one_p)
    else:
        min_six_p = min(min_six_p, six_p)
    min_one_p = min(min_one_p, one_p)

print(min(math.ceil(N/6)*min_six_p, N//6*min_six_p+N%6*min_one_p))

explain = """
목록중에서 6개를 살때 최소와 한개를 살때 최소값을 기록해둔다. 이때, 1개짜리를 6개 샀을 때, 최소가 될 수 있으니
이도 체크해서 최소값을 구한다.
"""