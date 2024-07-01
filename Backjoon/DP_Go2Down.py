import sys

N = int(sys.stdin.readline())
max_board = list(map(int, sys.stdin.readline().split()))
min_board = max_board

move = [-1, 0, 1]
for i in range(N-1):
    temp = list(map(int, sys.stdin.readline().split()))
    new_max = [0 for _ in range(3)]
    new_min = [1000000 for _ in range(3)]
    for j in range(3):
        for k in move:
            next = j+k
            if 0<=next < 3:
                 new_max[next] = max(new_max[next], temp[next] + max_board[j])
                 new_min[next] = min(new_min[next], temp[next] + min_board[j])

    max_board = new_max
    min_board = new_min
print(max(max_board), end=' ')
print(min(min_board))
