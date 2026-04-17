import sys

def check_root(number):
    number = int(number)
    cri = int(number**0.5)
    if cri **2 == number:
        return True
    return False


N, M = map(int, sys.stdin.readline().split())

board = []
for _ in range(N):
    row = sys.stdin.readline().strip()
    board.append(row)


answer = -1

for i in range(N):
    for j in range(M):
        if check_root(board[i][j]):
            answer = max(answer, int(board[i][j]))
        for row_dist in range(-(N-1), N):
            for column_dist in range(-(M-1), M):
                if row_dist == 0 and column_dist == 0:
                    continue
                temp = ""
                cur_r, cur_c = i, j

                while 0<=cur_r<N and 0<= cur_c <M:
                    temp += board[cur_r][cur_c]
                    if check_root(temp):
                        answer = max(answer, int(temp))
                    cur_r += row_dist
                    cur_c += column_dist


print(answer)


explain = """Brute force with quadra for-loop."""