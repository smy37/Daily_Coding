import sys

coin_num, final_cost = map(int, sys.stdin.readline().rstrip().split())

coin_list = []

for i in range(coin_num):
    temp = int(sys.stdin.readline().rstrip())
    if final_cost // temp != 0:
        coin_list.append(temp)
    else:
        break

coin_list = coin_list[-1::-1]

coin_count = 0
for i in coin_list:

    if final_cost == 0:
        break
    else:
        coin_count += final_cost // i
        final_cost = final_cost%i


print(coin_count)