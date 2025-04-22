import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(666, 100000000):
    if len(str(i).split('666')) != 1:
        cnt +=1

    if cnt == n:
        print(i)
        sys.exit()