import sys

num_line = int(sys.stdin.readline())


line_list = []
for i in range(num_line):
    line_list.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

real_list = []
for i in sorted(line_list):
    real_list.append(i[1])


test = [real_list[0]]

for i in range(1, num_line):
    if real_list[i] > test[-1]:
        test.append(real_list[i])
    else:
        for k,v in enumerate(test):
            if v > real_list[i]:
                test[k] = real_list[i]
                break


print(num_line-len(test))
