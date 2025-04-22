import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    board = []
    for _ in range(2):
        t = list(map(int, sys.stdin.readline().split()))
        board.append(t)
    u_max = board[0][0]
    d_max = board[1][0]
    for i in range(1,N):
        board[0][i] = d_max + board[0][i]
        board[1][i] = u_max + board[1][i]
        u_max = max(u_max, board[0][i])
        d_max = max(d_max, board[1][i])
    print(max(u_max, d_max))

    )