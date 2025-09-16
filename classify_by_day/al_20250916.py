import sys

num_list = []

while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    num_list.append(n)

upper_limit = max(num_list)
dp = [0]*(upper_limit+1)