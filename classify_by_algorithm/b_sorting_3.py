import sys

iter_num = int(sys.stdin.readline())

final_result = {}
for i in range(iter_num):
    temp = int(sys.stdin.readline())
    if temp not in final_result:
        final_result[temp] = 1

    else:
        final_result[temp] +=1


for i in sorted(final_result):
    for j in range(final_result[i]):
        print(i)
