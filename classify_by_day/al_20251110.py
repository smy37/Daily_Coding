import sys
from collections import deque

T = int(sys.stdin.readline())
ori_num_l = []
for _ in range(T):
    ori_num_l.append(int(sys.stdin.readline()))

num_l = sorted(ori_num_l)
num_d = {i: [] for i in num_l}

dq = deque()
dq.append([1, [1]])
cal = ["+", "-", ""]

while dq:
    idx, cur = dq.popleft()

    if idx == num_l[-1]:
        break

    for c in cal:
        n_cur = cur + [c, idx+1]
        sum_exp = "".join(map(str, n_cur))
        sum_val = eval(sum_exp)

        if idx+1 in num_d and sum_val == 0:
            num_d[idx+1].append(n_cur)
        dq.append([idx+1, n_cur])

for n in ori_num_l:
    t_l = []
    for candi in num_d[n]:
        temp = ""
        for c in candi:
            if c == "":
                temp += " "
            else:
                temp += str(c)
        t_l.append(temp)
    t_l.sort()
    for t in t_l:
        print(t)
    print()

explain = """
BFS를 이용햬서 수형도를 그리는 방식을 이용하였다. 매 연산자 마다 3개씩 가지가 뻣어나가고 이는 BFS를 통해 모든 케이스를 체크 가능하다.
그래프탐색, 재귀, 트리, 수형도는 밀접한 관계가 있다는 것을 유의해두면 좋다.
"""
