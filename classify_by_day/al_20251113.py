import sys

N = int(sys.stdin.readline())

num_l = []
num_dict = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    num_l.append(num)


next_num_l = sorted(num_l, reverse=True)

for i in range(N):
    if next_num_l[i] not in num_dict:
        num_dict[next_num_l[i]] = 0
        for j in range(i+1, N):
            if next_num_l[i]%next_num_l[j] == 0:
                num_dict[next_num_l[i]] += 1


for n in num_l:
    print(num_dict[n])



