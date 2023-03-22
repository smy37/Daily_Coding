import sys

n = int(sys.stdin.readline())
board = [[0 for _ in range(n)] for _ in range(n)]
order = {}
for i in range(n):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    for j in range(n):
        order[(i,j)] = temp[j]

order = dict(sorted(order.items(), key = lambda x : x[1], reverse= True))

x_p = [1,-1,0,0]
y_p = [0,0,-1,1]
ans = 1
for i in order:
    t =list(i)
    t_n = order[i]
    t_x, t_y = t[0], t[1]
    board[t_x][t_y] = 1
    for j in range(4):
        n_x = t_x + x_p[j]
        n_y = t_y + y_p[j]
        if 0<= n_x < n and 0<= n_y < n:
            if order[(n_x,n_y)] > t_n:
                board[t_x][t_y] = max(board[t_x][t_y], 1+board[n_x][n_y])
                ans = max(ans, board[t_x][t_y])

print(ans)