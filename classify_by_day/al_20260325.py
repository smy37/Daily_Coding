import sys

N, C = map(int, sys.stdin.readline().split())
w_list = list(map(int, sys.stdin.readline().split()))
w_list.sort()


### First Approach
# for i, w in enumerate(w_list):
#     left, right = i+1, N+1
#
#     rest = C-w
#     while left < right:
#         cur_w = w_list[left] + w_list[right]
#         if rest < cur_w:
#             right -= 1
#         elif rest > cur_w:
#             left += 1
#         else:
#             print(1)
#             sys.exit()
#     if w_list[i+1] + w_list[i+2] > C:
#         break
# print(0)


### Second Approach
for w in w_list:
    if w == C:
        print(1)
        sys.exit()

left, right = 0, N-1

while left < right:
    cur_weight = w_list[left] + w_list[right]

    if cur_weight > C:
        right -=1
    elif cur_weight < C:
        left += 1
    else:
        print(1)
        sys.exit()


for i, w in enumerate(w_list):
    left, right = i+1, N-1
    rest = C-w
    while left < right:
        cur_weight = w_list[left] + w_list[right]
        if rest > cur_weight:
            left += 1
        elif rest < cur_weight:
            right -= 1
        else:
            print(1)
            sys.exit()
print(0)