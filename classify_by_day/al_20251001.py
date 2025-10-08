import sys 

N = int(sys.stdin.readline())
cord_l = []
foul_l = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())

    if x >= 0:
        if x > y:
            foul_l.append([x,y])
        else:
            cord_l.append(x**2+y**2)
    else:
        if -x > y:
            foul_l.append([x,y])
        else:
            cord_l.append(x**2+y**2)

Q = int(sys.stdin.readline())

for _ in range(Q):
    r = int(sys.stdin.readline())
    hit_cnt = 0
    for d in cord_l:
        if d <= r**2:
            hit_cnt += 1

    print(len(foul_l), hit_cnt, len(cord_l)-hit_cnt)

