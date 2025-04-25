import sys 

move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def check_divide(candidate, board, N, M):
    visited = {}
    for c in candidate:
        s = [c]
        visited = {c: True}
        while s:
            t = s.pop()
            for i in range(4):
                nx, ny = t[0] + move[i][0], t[1] + move[i][1]
                if 0<= nx < N and 0<= ny < M and (nx, ny) not in visited and board[nx][ny] != 0:
                    visited[(nx, ny)] = True
                    s.append((nx, ny))
        break

    if len(visited) == len(candidate):
        return True
    return False

N, M = map(int, sys.stdin.readline().split())

board = []
candidate = {}

for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    for j in range(len(t)):
        if t[j] != 0:
            candidate[(i, j)] = True
    board.append(t)

year = 0

while True:
    if not check_divide(candidate, board, N, M):
        print(year)
        break
    elif len(candidate) == 0:
        print(0)
        break
    del_l = []
    for c in candidate:
        cnt = 0
        for i in range(4):
            nx, ny = c[0]+move[i][0], c[1] + move[i][1]

            if 0<=nx <N and 0<=ny < M and (nx, ny) not in candidate:
                cnt +=1
        if cnt >= board[c[0]][c[1]]:
            board[c[0]][c[1]] = 0
            del_l.append(c)
        else: 
            board[c[0]][c[1]] -= cnt
    for d in del_l:
        del candidate[d]
    year += 1

    