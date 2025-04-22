import sys


test_case = int(sys.stdin.readline())
for i in range(test_case):
    length = int(sys.stdin.readline())
    temp_list = list(map(int, sys.stdin.readline().split(' ')))
    print(temp_list)