import sys
import math 

N = int(sys.stdin.readline())

### 1. Fisrt Approach
# num_l = []
# num_dict = {}
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     num_l.append(num)


# next_num_l = sorted(num_l, reverse=True)

# for i in range(N):
#     if next_num_l[i] not in num_dict:
#         num_dict[next_num_l[i]] = 0
#         for j in range(i+1, N):
#             if next_num_l[i]%next_num_l[j] == 0:
#                 num_dict[next_num_l[i]] += 1


# for n in num_l:
#     print(num_dict[n])


### 2. Second Approach
num_dict = {}
num_l = []
for i in range(N):
    num = int(sys.stdin.readline())
    num_l.append(num)

    if num not in num_dict:
        num_dict[num] = 0
    num_dict[num] += 1

checked = {}

for n in num_l:
    if n in checked:
        print(checked[n])
    else:
        temp = 0
        for i in range(1, int(math.sqrt(n))+1):
            if n % i == 0 and i in num_dict:
                rest = n//i
                temp += num_dict[i]
                if i != rest and rest in num_dict:
                    temp += num_dict[rest]
        checked[n] = temp-1
        print(checked[n])

