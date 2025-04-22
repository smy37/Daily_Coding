import sys
import copy


def rotation(x : int, y : int, direc : int) -> int:
    if direc == 1:
        return -y, x
    elif direc == 2:
        return -x, -y
    elif direc == 3:
        return y, -x
    elif direc == 0:
        return x, y


def rotate_matrix(arr : list) -> list:
    n_mat = copy.deepcopy(arr)      ## 처음에 n_mat을 카피한다음에 아래에서 arr에 대한 연산을 진행주었음... arr& 로 Input을 받기 때문에 원본이 수정됨.

    dx = int(arr[-1][0])
    dy = int(arr[-1][1])

    for i in range(len(n_mat)):
        n_mat[i][0] -= dx
        n_mat[i][1] -= dy

    for i in range(len(n_mat)):
        n_mat[i][0], n_mat[i][1] = rotation(n_mat[i][0], n_mat[i][1], 3)

    for i in range(len(n_mat)):
        n_mat[i][0] += dx
        n_mat[i][1] += dy

    for i in range(len(n_mat)-2, -1, -1):
        arr.append(n_mat[i])

    return arr

def make_dragon():
    final = []
    t = [[0,0], [1, 0]]
    final.append(copy.deepcopy(t))
    for i in range(10):
        t = rotate_matrix(t)    ## 이부분과 rotate_matrix안에서 입력으로 받은 리스트를 수정하는 코드는 예상치 못한 에러를 발생시킨다.
        final.append(copy.deepcopy(t))

    return final

def make_dir_dragon(d_list_g : list, direc : int ) -> list:
    for i in range(len(d_list_g)):
        d_list_g[i][0], d_list_g[i][1] = rotation(d_list_g[i][0], d_list_g[i][1], direc)
    return

def check_board(board : list, dList : list, x : int, y : int, direc : int, gene : int):
    tt = copy.deepcopy(d_list[gene])
    make_dir_dragon(tt, direc)

    for i in range(len(tt)):
        n_x = x + tt[i][0]
        n_y = y - tt[i][1]
        board[n_y][n_x] = 1
    return

d_list = make_dragon()

answer = 0
board=[[0 for _ in range(101)] for _ in range(101)]
curve_num = int(sys.stdin.readline())
for _ in range(curve_num):
    temp = list(map(int, sys.stdin.readline().split()))
    x, y, direc, gene = temp[0], temp[1], temp[2], temp[3]
    check_board(board, copy.deepcopy(d_list), x, y, direc, gene)

for i in range(100):
    for j in range(100):
        if board[i][j] == 1 and board[i+1][j] ==1 and board[i][j+1] ==1 and board[i+1][j+1] ==1:
            answer +=1

print(answer)