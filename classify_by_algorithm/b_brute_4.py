import sys

m, n = map(int, sys.stdin.readline().split(' '))

cri = 8


ex1 = []
ex2 = []

for i in range(8):
    board_1 = []
    board_2 = []
    for j in range(8):
        if i%2 == 0 and j%2 == 0:
            board_1.append('W')
            board_2.append('B')
        elif i %2 == 0 and j%2 != 0:
            board_1.append('B')
            board_2.append('W')
        elif i%2 != 0 and j%2 ==0 :
            board_1.append('B')
            board_2.append('W')
        elif i %2 != 0 and j%2 !=0 :
            board_1.append('W')
            board_2.append('B')

    ex1.append(board_1)
    ex2.append(board_2)

test_board = []
for i in range(m):
    test_board.append(list(sys.stdin.readline().strip()))


final = 1000000
for i in range(m-8+1):
    for j in range(n-8+1):
        cnt1 = 0
        cnt2 = 0
        for a in range(cri):
            for b in range(cri):
                if test_board[a+i][b+j] != ex1[a][b]:
                    cnt1 +=1
                else:
                    cnt2 +=1
        temp = min(cnt1, cnt2)
        if final > temp:
            final = temp
        if final == 0 :
            print(0)
            sys.exit()

print(final)