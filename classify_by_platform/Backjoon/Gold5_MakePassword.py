import sys
from itertools import combinations

pw_list = []

L, C = map(int, sys.stdin.readline().split())

w_list = list(sys.stdin.readline().split())
w_list = sorted(w_list)

moam = []
jaum = []

for i in w_list:
    if i in ['a', 'e', 'i', 'o', 'u']:
        moam.append(i)
    else:
        jaum.append(i)

for i in range(1, C-1):
    j_cnt = L-i
    if len(moam) >= i and len(jaum)>= j_cnt >= 2:
        moam_c = combinations(moam, i)

        for j in moam_c:
            t_m = ''.join(j)
            jaum_c = combinations(jaum, j_cnt)
            for k in jaum_c:
                t_j = ''.join(k)
                pw_list.append(''.join(sorted(t_m+t_j)))

pw_list = sorted(pw_list)

for i in pw_list:
    print(i)