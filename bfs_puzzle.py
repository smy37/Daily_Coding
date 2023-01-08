from collections import deque
import sys
import copy

game_b1 = [[0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0], [0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
table1 = [[1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0], [0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1], [1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]]

def rot_trans(test1, test2, cri):
    answer = 0
    n1 = []
    for i in test1:
        temp = []
        for j in i:
            temp.append([j//cri, j%cri])
        n1.append(temp)
    n1 = sorted(n1)

    for i in range(len(n1)):    ## i 조각 한개
        n1[i] = sorted(n1[i])
        c_x = n1[i][0][0]
        c_y = n1[i][0][1]
        for j in range(len(n1[i])):
            n1[i][j][0] -= c_x
            n1[i][j][1] -= c_y

    n2 = []
    for i in test2:
        temp = []
        for j in i:
            temp.append([j//cri, j%cri])
        n2.append(temp)
    n2 = sorted(n2)
    dup_check = []


    for i in range(len(n1)):
        for j in range(len(n2)):    ## j는 조각 하나를 의미한다.
            if j not in dup_check:
                if convert(copy.deepcopy(n2[j]), 0) == sorted(n1[i]):
                    answer += len(n1[i])
                    dup_check.append(j)

                    break
                elif convert(copy.deepcopy(n2[j]), 1) == sorted(n1[i]):
                    answer += len(n1[i])
                    dup_check.append(j)

                    break
                elif convert(copy.deepcopy(n2[j]), 2) == sorted(n1[i]):

                    answer += len(n1[i])
                    dup_check.append(j)

                    break
                elif convert(copy.deepcopy(n2[j]), 3) == sorted(n1[i]):

                    answer += len(n1[i])
                    dup_check.append(j)

                    break

    return answer
def convert(piece, ver):
    for i in range(len(piece)):
        if ver == 0:
            a = -piece[i][1]
            b = piece[i][0]
            piece[i][0] = a
            piece[i][1] = b
        elif ver == 1:
            a = -piece[i][0]
            b = -piece[i][1]
            piece[i][0] = a
            piece[i][1] = b

        elif ver == 2:
            a = piece[i][1]
            b = -piece[i][0]
            piece[i][0] = a
            piece[i][1] = b
        elif ver == 3:
            continue

    piece = sorted(piece)


    c_x = piece[0][0]
    c_y = piece[0][1]
    for i in range(len(piece)):
        piece[i][0] -= c_x
        piece[i][1] -= c_y

    return piece

def solution(game_bb, table):
    cri = len(game_bb)
    test1 = get_puzzle(game_bb, 0)
    test2 = get_puzzle(table, 1)
    t1 = [[89, 90, 101, 102, 114, 126]]
    t2 = [[75, 87, 99, 100, 111, 112]]
    rot_trans(t1, t2, cri)
    answer = rot_trans(test1, test2, cri)
    return answer

def get_puzzle(game_b, ver):
    final_puzzle = []
    length = len(game_b)
    visited = []
    for i in range(len(game_b)):
        for j in range(len(game_b[i])):
            num = i*length + j
            if num not in visited:
                if game_b[i][j] == ver:
                    dq = deque()
                    temp_visit = []
                    dq.append(num)
                    while dq:
                        t_num = dq.popleft()
                        row = t_num // length
                        column = t_num % length
                        if t_num not in temp_visit:
                            visited.append(t_num)
                            temp_visit.append(t_num)
                            for k in range(4):
                                n_row, n_column = -1, -1
                                if k ==0:
                                    n_row = row - 1
                                    n_column = column
                                elif k ==1:
                                    n_row = row + 1
                                    n_column = column
                                elif k ==2:
                                    n_row = row
                                    n_column = column -1
                                elif k ==3:
                                    n_row = row
                                    n_column = column +1
                                if (n_row >=0 and n_row < length) and (n_column>=0 and n_column < length) and game_b[n_row][n_column] == ver and n_row*length + n_column not in temp_visit:
                                    dq.append(n_row*length +n_column)

                    final_puzzle.append(sorted(temp_visit))
    return final_puzzle

print(solution(game_b1, table1))