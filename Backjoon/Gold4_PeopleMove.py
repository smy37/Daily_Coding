import sys
from collections import deque

N, L, R = map(int, sys.stdin.readline().split())

board = []

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    board.append(temp)

flag = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0
while flag:
    visited = {}
    flag = False
    for i in range(N):
        for j in range(N):

            if (i,j) not in visited:
                sum_temp = [[i,j]]
                dq = deque()
                dq.append([i,j])
                visited[(i,j)] = 1
                while dq:
                    cx,cy = dq.popleft()
                    for k in range(4):
                        nx = cx+dx[k]
                        ny = cy+dy[k]
                        if 0<= nx < N and 0<= ny < N and (nx,ny) not in visited and (L<=abs(board[nx][ny]-board[cx][cy])<=R):
                            dq.append([nx,ny])
                            visited[(nx,ny)] = 1
                            sum_temp.append([nx,ny])
                            flag = True

                if len(sum_temp) > 1:
                    v = 0
                    for x in sum_temp:
                        v += board[x[0]][x[1]]
                    v = int(v/len(sum_temp))

                    for x in sum_temp:
                        board[x[0]][x[1]] = v
    if flag:
        answer +=1

print(answer)