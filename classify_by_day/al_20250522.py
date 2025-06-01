import sys

N = int(sys.stdin.readline())
money_account = list(map(int, sys.stdin.readline().split()))
J = int(sys.stdin.readline())
C = int(sys.stdin.readline())


### 1. First Method Using Probability
# prob = money_account[0]/sum(money_account)
# answer = prob*J*C+money_account[0]
# print(answer)


### 2. Second Method Using Dynamic Porgraaming
# dp = [money_account]
#
# for i in range(C):
#     t = dp[-1]
#     sum_t = sum(t)
#
#     next_t = [0 for _ in range(N)]
#     for j in range(len(t)):
#         next_t[j] = t[j]/sum_t*J + t[j]
#     dp.append(next_t)

explain = """
Dynamic programming을 이용해서 기대값을 누적해 나가는 방법과 확률를 거시적으로 바라보고 공식적으로 바로 답을 구하는 
두가지 방법 모두 가능하다. 먼저 첫번째 방법으로는 확률을 거시적으로 바라보는 방법을 사용했는데 결국 시작부터 C주후 까지 
첫번째 사람이 당첨되는 확률을 모두 더하면 0번째 주의 당첨될 확률 * C가 된다. 첫번째 사람 말고 다른 사람도 0번째 주의 확률을
기반으로 기댓값이 정해지므로 1주 후, 2주 후, 3주 후, 4주 후, 5주 후... C주 후에서 각 사람의 당첨될 확률은 변하지 않는다.
두번째 방법으로는 Dynamic Programming을 이용해서 각 주마다의 기대값을 이전 주의 누적된 값으로 계산하는 방법을 사용하였는데 
결국 1주 후부터는 각사람의 실제 금액이 아닌 기대값 금액이 되지만 이 기대값 금액으로 구한 확률을 누적시킨 것이 최종 기대값이 된다는
것을 이용하는 것이다. 
"""