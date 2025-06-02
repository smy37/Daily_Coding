import sys
import math

N, K = map(int, sys.stdin.readline().split())

### 1. First Method -> Failed
# def get_left_str(criteria):
#     left_a = 0
#     left_b = 0
#     for i in range(int(math.sqrt(criteria)), 0, -1):
#         if criteria %i == 0:
#             left_a = i
#             left_b = criteria//i
#             break
#     return left_a, left_b
#
# temp = ""
# if K %2 == 0:
#     cri = K
#     l_a, l_b = get_left_str(cri)
#     temp += "A"*l_a + "B"*l_b
# else:
#     cri = K-1
#     l_a, l_b = get_left_str(cri)
#     temp += "A" * l_a + "B" * (l_b-1)
#     temp += "AB"
#
# if len(temp) > N:
#     print(-1)
# else:
#     temp += "A"*(N-len(temp))
#     print(temp)

### 2. Second Method
answer = ""
for i in range(1, N+1):
    a_cnt = i
    b_cnt = N-i
    cur_k = a_cnt*b_cnt

    if cur_k < K:
        continue
    cur_str = ["A"]*a_cnt + ["B"]*b_cnt
    a_idx = a_cnt-1

    while cur_k > K and a_idx >= 0:
        move = min(cur_k-K, b_cnt)
        cur_str[a_idx], cur_str[a_idx+move] = cur_str[a_idx+move], cur_str[a_idx]
        cur_k -= move
        a_idx -=1

    answer = "".join(cur_str)
    break
if len(answer) >0:
    print(answer)
else:
    print(-1)


explain= """
첫번째 시도에서는 K를 짝수로 만들고 해당 K의 약수중에서 K의 루트값을 안넘는 최대값을 구해서 A의 개수로 하고 나머지를 B의 개수로 하여
문자열을 구하는 시도를 하였다. 그러나, K가 큰 케이스 중에서는 약수가 작게 나오는 K=23 같은 경우에는 실제로는 N이 10일경우 만족하는
문자열을 만들 수 있지만 첫번째 로직에서는 -1을 출력하게 된다. 
따라서 두번째 시도에서는 1부터 N까지의 A개수에서 A개수 * B개수를 한것이 K 이상인 경우에 대해서 일단 A를 왼쪽에 몰고 B를 오른쪽에
몬 후에 가장 오른쪽에 있는 A부터 K가 되도록 오른쪽으로 옮기는 로직을 사용하였다. 
"""