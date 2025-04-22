import sys

### Solved 1.
# t = int(sys.stdin.readline())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     like_l = list(map(int,sys.stdin.readline().strip().split(' ')))
#     cnt_d = {}
#     g = 0
#     for i in range(len(like_l)):
#         if i+1 == like_l[i]:
#             g += 1
#         else:
#             cnt_d[i+1] = like_l[i]
#     while len(cnt_d) > 0:
#         temp = {}
#         cur = list(cnt_d.keys())[0]
#         temp[cur] = 1
#         idx = 2
#         flag = True
#
#         while flag:
#             if cnt_d[cur] not in temp:
#                 if cnt_d[cur] not in cnt_d:
#                     flag = False
#                     break
#                 temp[cnt_d[cur]] = idx
#                 idx += 1
#                 cur = cnt_d[cur]
#             else:
#                 flag = False
#                 g += len(temp) - temp[cnt_d[cur]] +1
#         for i in temp:
#             cnt_d.pop(i)
#
#     print(n-g)


### Solved 2.
def dfs(num):
    global ans
    visited[num-1] = True
    stack.append(num)
    next = like_l[num-1]
    if visited[next-1] == True:
        if next in stack:

            ans += len(stack) -stack.index(next)

        return
    else:
        dfs(next)
    return

t = int(sys.stdin.readline())
for _ in range(t):
    ans = 0
    n = int(sys.stdin.readline())
    like_l = list(map(int, sys.stdin.readline().strip().split(' ')))
    visited =[False for _ in range(n)]

    for i in range(n):
        if visited[i] == False:
            stack = []
            dfs(i+1)
    print(n-ans)

### 인터넷에 나와있는 풀이를 많이 참조하였음...
### 재귀를 이용하지않고 스택을 이용한 dfs 구현으로 복습 진행해야함....