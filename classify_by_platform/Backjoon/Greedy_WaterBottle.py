import sys

n, k = map(int, sys.stdin.readline().split())

b_v = bin(n)[2:]
cnt = 0
cri = -1
if b_v.count("1") <= k:
    print(0)
    sys.exit()
for i in range(len(b_v)):
    if b_v[i] == "1":
        cnt +=1

    if cnt == k:
        cri = i
        break

print(int("1"+"0"*(len(b_v)-cri),2)-int(b_v[cri:],2))