import sys

node_num = int(sys.stdin.readline())
edge_num = int(sys.stdin.readline())

inf = 100000001
board = [[inf for _ in range(node_num)] for _ in range(node_num)]

for i in range(edge_num):
    s, e, w = map(int, sys.stdin.readline().strip().split())
    board[s-1][e-1] = min(board[s-1][e-1], w)

for i in range(node_num):
    board[i][i] = 0

for i in range(node_num):
    for j in range(node_num):
        for k in range(node_num):
            if j!= k:
                board[j][k] = min(board[j][k], board[j][i] + board[i][k])

for i in board:
    for j in i:
        if j == inf:
            print(0, end = ' ')
        else:
            print(j, end = ' ')
    print()