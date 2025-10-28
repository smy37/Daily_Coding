import sys 

K = int(sys.stdin.readline())
for _ in range(K):
    cur_num = list(map(int, sys.stdin.readline()))
    g1, g2 = cur_num[:4], cur_num[4:]
    