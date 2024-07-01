import sys


N, K = map(int, sys.stdin.readline().split())

### Method 1
# target_num = []
# ini_str = sys.stdin.readline().strip()
#
# for i in ini_str:
#     target_num.append(int(i))
#
# answer = ''
# while K > 0:
#     temp = target_num[:K+1]
#     max_num = max(temp)
#     max_loc = temp.index(max_num)
#     K -= max_loc
#     answer += str(max_num)
#     target_num = target_num[max_loc+1:]
#
# for i in target_num:
#     answer += str(i)


### Method 2
ini_str = sys.stdin.readline()
s = []
n = -1
length = N-K
for i in range(N):
    n = int(ini_str[i])
    if len(s) == 0:
        s.append(n)
    else:
        while s and K > 0:
            if s[-1] >= n:
                s.append(n)
                break
            else:
                s.pop()
                K-=1
        if len(s) == 0:
            s.append(n)
    if K == 0:
        break
s.append(n)

for j in range(i+1, N-K):
    s.append(ini_str[j])
s = s[:length]
answer = ''
for i in s:
    answer += str(i)
print(answer)