import sys

N = int(sys.stdin.readline())

num_l_p = []
num_l_m = []
one_l = []
flag = False

for i in range(N):
    t = int(sys.stdin.readline())
    if t > 1:
        num_l_p.append(t)
    elif t <= 0:
        num_l_m.append(t)
    else:
        flag = True
        one_l.append(1)
num_l_p = sorted(num_l_p, reverse= True)
num_l_m = sorted(num_l_m)

answer = 0
for i in range(len(num_l_p)//2):
    answer += (num_l_p[2*i]*num_l_p[2*i+1])
if len(num_l_p)%2 != 0:
    answer += num_l_p[-1]
for i in range(len(num_l_m)//2):
    answer += (num_l_m[2*i]*num_l_m[2*i+1])
if len(num_l_m)%2 != 0:
    answer += num_l_m[-1]

if flag:
    answer += sum(one_l)

print(answer)