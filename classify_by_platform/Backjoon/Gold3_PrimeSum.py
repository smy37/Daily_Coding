import sys

n = int(sys.stdin.readline())
p_list = []


### Method 1. Brute Force
p_list = [1 for _ in range(n+1)]

for i in range(2, n+1):
    if p_list[i] == 0:
        continue
    else:
        for j in range(2, n//i+1):
            p_list[i*j] = 0

p_list[0] = 0
p_list[1] = 0

compact_p = []
pre = 0
for i in range(len(p_list)):
    if p_list[i]:
        if pre + i > n:
            break
        compact_p.append(i)
        pre = i

if p_list[-1] and n!=2:
    compact_p.append(n)

del p_list

ans = 0

for i in range(len(compact_p)):
    temp_sum = 0
    for j in range(i, len(compact_p)):
        temp_sum += compact_p[j]
        if temp_sum > n:
            break
        elif temp_sum == n:
            ans += 1
            break
print(ans)
