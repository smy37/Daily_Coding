import sys
from queue import PriorityQueue
m, n = map(int, sys.stdin.readline().strip().split(' '))

array = []

for i in range(m):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    array.append(temp)


que = PriorityQueue()
que.put((-array[0][0], [0,0]))
score = []

for i in range(m):
    score.append([0]*n)
score[0][0] = 1


while que.qsize() != 0:
    t = que.get()
    value = t[0]
    temp = t[1]
    if temp == [m-1, n-1]:
        break
    x_c = temp[1]
    y_c = temp[0]

    ## 1. 서쪽
    if x_c-1 >= 0:
        if value < -array[y_c][x_c-1]:
            if score[y_c][x_c-1] == 0:
                que.put((-array[y_c][x_c-1], [y_c,x_c-1]))
            score[y_c][x_c-1] += score[y_c][x_c]
    ## 2. 동쪽
    if x_c+1 < n:
        if value < -array[y_c][x_c+1]:
            if score[y_c][x_c+1] == 0:
                que.put((-array[y_c][x_c+1], [y_c,x_c+1]))
            score[y_c][x_c+1] += score[y_c][x_c]
    ## 3. 남쪽
    if y_c -1 >= 0:
        if value < -array[y_c-1][x_c]:
            if score[y_c-1][x_c] == 0:
                que.put((-array[y_c-1][x_c], [y_c-1,x_c]))
            score[y_c-1][x_c] += score[y_c][x_c]
    ## 4. 북쪽
    if y_c +1 < m:
        if value < -array[y_c+1][x_c]:
            if score[y_c+1][x_c] == 0:
                que.put((-array[y_c+1][x_c], [y_c+1,x_c]))
            score[y_c+1][x_c] += score[y_c][x_c]

print(score[m-1][n-1])

