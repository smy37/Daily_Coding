import sys
from collections import deque


N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

candidate = {n:[-1,-1] for n in num_list}
make_l = {}
for n in num_list:
    if n*2 in num_list:
        candidate[n][0] = n*2
        make_l[n*2] = 1
    if n%3 == 0 and n//3 in num_list:
        candidate[n][1] = n//3
        make_l[n//3] = 1

s = -1
for n in num_list:
    if n not in make_l:
        s = n
        break
answer = [s]

for i in range(N-1):
    t = answer[i]
    if candidate[t][0] != -1:
        answer.append(candidate[t][0])
        candidate[t][0]= -1
    elif candidate[t][1] != -1:
        answer.append(candidate[t][1])
        candidate[t][1] = -1

for i in answer:
    print(i, end=" ")

explain = """
문제 풀이의 핵심 개념은 특정 수를 기반으로 *2 연산과 /3 연산을 수행했을 때, 생성되는 수들은 절대 겹치지 않는다는 것이다.
만약 겹치려면 같은수로 곱하고 나누는 과정이 필요하다. 해당 문제의 연산에서는 서로 다른 2로 곱하고 3으로 나누는 것이라
연산을 통해 생성되는 수들이 겹치지 않는다. 그리고 첫번째 수를 제외한 두번째부터 N번째 까지의 수는 모두 처음에 주어지는 배열에서
만들 수 있는 수이다. 따라서 첫번째 수를 구하기 위해서는 주어진 배열의 수들로 만든 수들을 모은 집합에 속하지 않는 수를 구하면 된다.
수들이 겹치지 않으므로 특정 수에서 *2와 /3을 한 수가 모두 처음 주어진 배열에 있더라도 둘 중에 아무거나 선택해서 경로를 만들어도
둘다 답이 된다.
"""