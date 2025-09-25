import sys

N, M = map(int , sys.stdin.readline().split())

price = []
for _ in range(M):
    six_p, one_p = map(int, sys.stdin.readline().split())

    if 6*one_p < six_p:
        price.append([6*one_p, one_p])
    else:
        price.append([six_p, one_p])