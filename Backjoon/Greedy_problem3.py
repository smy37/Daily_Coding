import sys

num_people = int(sys.stdin.readline())
time_list = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
final = 0
for k,i in enumerate(range(num_people, 0, -1)):
    final+= time_list[k]*i
print(final)