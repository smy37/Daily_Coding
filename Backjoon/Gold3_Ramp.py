import sys

N, L = map(int, sys.stdin.readline().strip().split(' '))

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split(' '))))




answer = 0


### 1. 행에 대한 체크
for i in range(N):
    cri = board[i][0]
    cur = 0
    move = 0
    flag = True
    while move < N:
        if cri == board[i][move]:
            move += 1
        elif cri +1 == board[i][move]:
            if move - cur >= L:
                cur = move
                cri = board[i][move]
                move += 1
            else:
                flag = False
                break
        elif cri -1 == board[i][move]:
            flag2 = True
            for j in range(move, move + L):
                if j < N:
                    if board[i][j] != cri -1:
                        flag2 = False
                        break
                else:
                    flag = False
                    break
            if flag2:
                cur = move + L
                cri = board[i][move]
                move += L
            else:
                flag = False
                break
        else:
            flag = False
            break
    if flag:
        # print('행에 대해서: ', i)
        answer +=1

### 2. 열에 대한 체크
for i in range(N):
    cri = board[0][i]
    cur = 0
    move = 0
    flag = True
    while move < N:
        if cri == board[move][i]:
            move += 1
        elif cri +1 == board[move][i]:
            if move - cur >= L:
                cur = move
                cri = board[move][i]
                move += 1
            else:
                flag = False
                break
        elif cri -1 == board[move][i]:
            flag2 = True
            for j in range(move, move + L):
                if j < N:
                    if board[j][i] != cri -1:
                        flag2 = False
                        break
                else:
                    flag = False
                    break
            if flag2:
                cur = move + L
                cri = board[move][i]
                move += L
            else:
                flag = False
                break
        else:
            flag = False
            break

    if flag:
        # print('열에 대해서: ', i)
        answer +=1
print(answer)