import sys

N = int(sys.stdin.readline())

### 1. 첫번째 접근 방법
# s = deque([])
# for i in range(9):
#     t = [0]*10
#     t[i+1] = 1
#     s.append([i+1, t])
# answer = [0]*10
# while s:
#     t = s.popleft()
#     if t[0] > N:
#         break
# 
#     for i in range(10):
#         tt = copy.deepcopy(t[1])
#         tt[i] += 1
#         t_num = int(str(t[0]) + str(i))
#         s.append([t_num, tt])
#         answer[i] += t[1][i]
# 
# for i in answer:
#     print(i, end=' ')


### 2. 두번째 접근 방법 

num_len = len(str(N))

cur = N
num_cnt = {i:0 for i in range(10)}
for i in range(num_len):
    cur_n = cur % 10

    left = N // (10**(i+1))
    right = N % (10**(i))

    if right == 0:
        for j in range(cur_n+1):
            num_cnt[j] += left+1
        for j in range(cur_n+1, 10):
            num_cnt[j] += left
    elif left == 0:
        for j in range(1, cur_n):
            num_cnt[j] += 10**len(str(right))
        num_cnt[cur_n] += right +1
    else:
        num_cnt[0] += left*(10**(len(str(right))))
        for j in range(1, cur_n):
            num_cnt[j] += (left+1)*(10**(len(str(right))))
        num_cnt[cur_n] += left * (10 ** (len(str(right)))) + right + 1
        for j in range(cur_n+1, 10):
            num_cnt[j] += left * (10 ** (len(str(right))))

    cur = cur//10

num_cnt[0] -= 1

print(num_cnt)