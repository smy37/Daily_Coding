import sys

city_len = int(sys.stdin.readline().rstrip())
road_len = list(map(int, sys.stdin.readline().rstrip().split()))
oil_list = list(map(int, sys.stdin.readline().rstrip().split()))

cur_min = []
final_sum = 0
cur_min.append(oil_list[0])
final_sum += cur_min[0]*road_len[0]

for k, v in enumerate(oil_list[:-1]):
    if k != 0:
        if v < cur_min[0]:
            cur_min[0] = v
        final_sum += cur_min[0]*road_len[k]
print(final_sum)