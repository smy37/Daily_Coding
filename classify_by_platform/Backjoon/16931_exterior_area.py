import sys

m, n = map(int, sys.stdin.readline().strip().split(' '))
paper = []

for i in range(m):
    paper.append(list(map(int, sys.stdin.readline().strip().split())))


area = 0
for i in range(m):
    for j in range(n):
        alt_x1 = [i-1, j]
        alt_x2 = [i+1, j]
        alt_y1 = [i, j-1]
        alt_y2 = [i, j+1]

        if alt_x1[0] ==-1:
            area += paper[i][j]
        else:
            if paper[alt_x1[0]][alt_x1[1]] < paper[i][j]:
                area +=  paper[i][j] - paper[alt_x1[0]][alt_x1[1]]
        if alt_x2[0] == m:
            area += paper[i][j]
        else:
            if paper[alt_x2[0]][alt_x2[1]] < paper[i][j]:
                area +=  paper[i][j] - paper[alt_x2[0]][alt_x2[1]]
        if alt_y1[1] ==-1:
            area += paper[i][j]
        else:
            if paper[alt_y1[0]][alt_y1[1]] < paper[i][j]:
                area +=  paper[i][j] - paper[alt_y1[0]][alt_y1[1]]
        if alt_y2[1] ==n:
            area += paper[i][j]
        else:
            if paper[alt_y2[0]][alt_y2[1]] < paper[i][j]:
                area +=  paper[i][j] - paper[alt_y2[0]][alt_y2[1]]

area += (2*m*n)

print(area)