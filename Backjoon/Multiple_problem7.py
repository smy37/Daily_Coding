import math
# import sys
#
# num_list = list(map(int, sys.stdin.readline().rstrip().split()))
#
#
# final = math.factorial(num_list[0]) / (math.factorial(num_list[1])*math.factorial(num_list[0]-num_list[1]))
#
# print(int(final))

for a in range(1, 11):
    for b in range(0, a+1):
        num_list = [a, b]
        final = 1
        for i in range(num_list[1]):
            final = final*(num_list[0]- i)/(num_list[1]-i)

        final2 = round(final)
        print(a, b)
        print(final, final2)
        print()