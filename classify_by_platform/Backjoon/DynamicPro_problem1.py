import sys

test_case = int(sys.stdin.readline())

for i in range(test_case):
    file_length = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().strip().split(' ')))
    result = 0
    while len(num_list) >2 :
        temp1 = num_list[0] + num_list[1]
        temp2 = num_list[1] + num_list[2]
        if temp1 >= temp2:
            num_list = [num_list[0]] + [temp2] + num_list[3:]
            result += temp2
        else:
            num_list = [temp1] + num_list[2:]
            result += temp1

    result += sum(num_list)

    print(result)
