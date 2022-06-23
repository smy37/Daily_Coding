import sys

cord_list = list(map(int, sys.stdin.readline().strip().split(' ')))

cordi = []
cnt = 0
for i in range(4):
    temp = []
    for j in range(2):
        temp.append(cord_list[cnt])
        cnt+=1
    cordi.append(temp)

x1, y1 = cordi[0][0], cordi[0][1]
x2, y2 = cordi[1][0], cordi[1][1]
x3, y3 = cordi[2][0], cordi[2][1]
x4, y4 = cordi[3][0], cordi[3][1]

a = y1 - y2
b = -x1 + x2
c = x1*y2 -x2*y1

v1 = a*x3 + b*y3 + c
v2 = a*x4 + b*y4 + c

if v1*v2 >= 0 :
    print(0)
else:
    print(1)
