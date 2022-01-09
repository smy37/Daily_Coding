import sys
import math


temp_num = int(sys.stdin.readline())

num_list = []

for i in range(temp_num):
    num_list.append(int(sys.stdin.readline()))

num_list = sorted(num_list, reverse=True)

revise_list = []

for k,v in enumerate(num_list[:-1]):
    revise_list.append(num_list[k] - num_list[k+1])

if len(revise_list) == 1:
    temp = revise_list[0]
    final_sum = []
    for i in range(2, int(math.sqrt(temp)) + 1):
        if temp % i == 0:
            final_sum.append(i)
            final_sum.append(temp // i)
    final_sum.append(temp)
    final_sum = list(set(final_sum))
    final_sum.sort()
    print(*final_sum)
    sys.exit()

elif len(revise_list) == 2:
    temp = math.gcd(revise_list[0], revise_list[1])
    final_sum = []
    for i in range(2, int(math.sqrt(temp))+1):
        if temp% i == 0:
            final_sum.append(i)
            final_sum.append(temp//i)
    final_sum.append(temp)
    final_sum = list(set(final_sum))
    final_sum.sort()
    print(*final_sum)
    sys.exit()

else:
    temp = math.gcd(revise_list[0], revise_list[1])

    for i in revise_list[2:]:
        temp = math.gcd(temp, i)

    final_num = []
    for i in range(2, math.ceil(math.sqrt(temp))+1):
        if temp%i == 0:
            final_num.append(i)
            final_num.append(temp//i)
    final_num.append(temp)
    final_num = list(set(final_num))
    final_num.sort()
    print(*final_num)