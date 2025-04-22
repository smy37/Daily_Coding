import sys

panel = []

iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    panel.append(temp)

start = [0,0]
length = iter_num

def dandc(s1, s2,l):
    for i in range(l):
        for j in range(l):
            if panel[s1+i][s2+j] != panel[s1][s2]:
                tem = l//2
                a1 = dandc(s1, s2, tem)
                a2 = dandc(s1+tem, s2, tem)
                a3 = dandc(s1, s2+tem, tem)
                a4 = dandc(s1+tem, s2+tem, tem)
                return [a1[0]+a2[0]+a3[0]+a4[0], a1[1]+a2[1]+a3[1]+a4[1]]

    if panel[s1][s2] == 0:
        return [1,0]
    elif panel[s1][s2] == 1:
        return [0,1]

answer = dandc(start[0],start[1], length)
print(answer[0])
print(answer[1])