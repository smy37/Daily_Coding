import sys

N = int(sys.stdin.readline())

### 1. First Approach
# for num_l in permutations([i+1 for i in range(N)]):
#     stack = []
#     flag = True
#     next_push = 1
#     for num in num_l:
#         while next_push <=N and (not stack or stack[-1] !=num):
#             stack.append(next_push)
#             next_push += 1
#         if stack[-1] != num:
#             flag = False
#             break
#         else:
#             stack.pop()
#     if flag:
#         print(" ".join([str(num) for num in num_l]))


### 2. Second Approach
def dfs(push_num, stack, output):
    if len(output) == N:
        print(" ".join(map(str, output)))
        return

    if stack:
        top = stack.pop()
        output.append(top)
        dfs(push_num, stack, output)
        output.pop()
        stack.append(top)

    if push_num <= N:
        stack.append(push_num)
        dfs(push_num +1, stack, output)
        stack.pop()

dfs(1, [], [])

explain = """
예상보다 많이 어려웠던 문제... 스택을 써야되는 경우면 시뮬레이션으로 가는 방법이 정답이 되는 경우가 많은거 같다.
첫번째 시도에서는 모든 순열 조합에 대해 해당 순열이 가능한지 판단하려고 했는데 시간초과가 발생하였다.
두번째 방법에서는 1부터 N까지 숫자를 넣으면서 바로 pop 하는 경우와 pop 하지 않는 경우를 가지치면서 수형도를 그려 탐색하였다.
사전 순으로 출력해야 하므로, pop하는 가지가 push 하는 가지보다 선행되야 한다.
"""