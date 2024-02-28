import sys
import copy
from collections import deque
r, c = map(int, sys.stdin.readline().split())

board = []
f_board = []
s_fire = deque()
dq = deque()

for i in range(r):
    t = sys.stdin.readline().strip()
    temp = [x for x in t]
    for j in range(c):
        if temp[j] == "F":
            s_fire.append([i,j,0])
        elif temp[j] == "J":
            dq.append([i,j,0])
    board.append(temp)

f_board = copy.deepcopy(board)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in s_fire:
    f_board[i[0]][i[1]] = '0'
while s_fire:
    t = s_fire.popleft()
    for i in range(4):
        nx = t[0] + dx[i]
        ny = t[1] + dy[i]
        if 0<=nx<r and 0<=ny<c and f_board[nx][ny] != '#':
            if (f_board[nx][ny] == '.' or f_board[nx][ny] == 'J'):
                f_board[nx][ny] = str(t[2]+1)
                s_fire.append([nx,ny,t[2]+1])
            else:
                if int(f_board[nx][ny]) > t[2]+1:
                    f_board[nx][ny] = str(t[2] + 1)
                    s_fire.append([nx, ny, t[2] + 1])

visited = {}
visited[(dq[0][0],dq[0][1])] = 0

while dq:
    t = dq.popleft()
    for i in range(4):
        nx = t[0] + dx[i]
        ny = t[1] + dy[i]
        if (0<=nx<r and 0<=ny<c) == False:
            print(t[2]+1)
            sys.exit()
        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == '.' and (nx,ny) not in visited:
            if f_board[nx][ny].isdigit() == True and t[2]+1 < int(f_board[nx][ny]):
                dq.append([nx,ny,t[2]+1])
                visited[(nx,ny)] = 0
            elif f_board[nx][ny].isdigit() != True:
                dq.append([nx, ny, t[2] + 1])
                visited[(nx, ny)] = 0

print("IMPOSSIBLE")


# Review
## 1. Visited(map)을 이용하여 재방문 체크하는 방법과 Board(List)에 숫자로 표시해서 재방문 체크하는 방법 혼용해서 사용
## 2. fire_board에 fire walk를 기입한 하나의 board를 이용하기까지 논리흐름 기억하기.
## 3. f_board에서 정수로 바꾸는 작업을 했지만 '.'과 '#' 모두 남아있을 수 있다는 점 기억.