import copy
import sys



#Problem 1.
# answer = 1
# r, c = map(int, sys.stdin.readline().strip().split(' '))
# board = []
#
# visited = set()
# for _ in range(r):
#     temp = sys.stdin.readline().strip()
#     board.append(temp)
#
#
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]
#
# def dfs(cr, visited, cur_len):
#     global answer
#     visited.add(ord(board[cr[0]][cr[1]]))
#     for i in range(4):
#         t_x = cr[1] + dx[i]
#         t_y = cr[0] + dy[i]
#         if 0<= t_x < c and 0<= t_y < r and ord(board[t_y][t_x]) not in visited:
#             dfs([t_y, t_x], visited, cur_len+1)
#     visited.remove(ord(board[cr[0]][cr[1]]))
#     answer = max(answer, cur_len)
#
# cur_str = board[0][0]
# cur = [0,0]
#
# visited.add(ord(cur_str))
#
# dfs(cur, visited, 1)
# print(answer)




### Map과 deepcopy를 이용한 방법이 시간 초과가 나는 이유....?
### Map + Deepcopy VS List + Slicing VS Set + 나중에 제거...  (나중에 제거 하는 방식은 Set 구조 외에 Map과 List 에도 적용 가능..?)
### DFS를 통한 재귀함수를 사용하는 방법 외에 BFS를 이용하는 방법.... 현재까지의 누적을 데이터에 포함시킨다면 가능...?
### 끝말잇기 문제를 BFS를 사용하는 법....


#Problem 2.
from collections import deque
max_v = 300000
V, E = map(int, sys.stdin.readline().strip().split(' '))
S = int(sys.stdin.readline().strip())
board = {}

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().strip().split(' '))
    if s not in board:
        board[s] = {}
        board[s][e] = w
    else:
        if e in board[s]:
            board[s][e] = min(board[s][e], w)
        else:
            board[s][e] = w

result = [max_v for _ in range(V)]

dq = deque()
dq.append(S)
result[S-1] = 0

while dq:
    temp = dq.popleft()
    if temp in board:
        for i in board[temp]:
            if board[temp][i] + result[temp-1] < result[i-1]:
                result[i-1] = board[temp][i]+result[temp-1]
                dq.append(i)



for i in result:
    if i!= max_v:
        print(i)
    else:
        print("INF")