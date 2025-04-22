import sys


diff_s = set()
diff_s.add(0)
N_w = int(sys.stdin.readline())
w_l = list(map(int, sys.stdin.readline().split()))

N_c = int(sys.stdin.readline())
c_l = list(map(int, sys.stdin.readline().split()))


for i in range(N_w):
    next_s = set()
    for j in diff_s:
        next_s.add(abs(j-w_l[i]))
        next_s.add(abs(j+w_l[i]))
    diff_s = diff_s | next_s

for c in c_l:
    if c in diff_s:
        print('Y', end=' ')
    else:
        print('N', end=' ')


