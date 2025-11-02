import sys 

num_l = [10]

for i in range(2, 11):
    temp = 1
    for j in range(i):
        temp *= ((10-j)/(j+1))
    num_l.append(int(temp))

N = int(sys.stdin.readline())

acc = 0
for i in range(len(num_l)):
    acc += num_l[i]

    if acc >= N:
        break

