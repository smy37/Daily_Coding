import sys

N = int(sys.stdin.readline())

num_list = []

for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
if N == 1:
    print(num_list[0])
    sys.exit()
answer = 0


## First Approach

# for i in range(0, N-1, 2):
#     if num_list[i+1] > 0:
#         if num_list[i] > 0:
#             start = i
#         else:
#             start = i+1
#             answer += num_list[i]
#         second_start = start
#         for j in range(start, N-1):
#             second_start = j
#             if num_list[j] > 1:
#                 break
#             else:
#                 answer += 1
#
#         if (N-1-second_start)%2 == 0:
#             for j in range(N - 1, second_start, -2):
#                 answer += num_list[j] * num_list[j - 1]
#             answer += num_list[second_start]
#         else:
#             for j in range(N - 1, second_start - 1, -2):
#                 answer += num_list[j] * num_list[j - 1]
#         break
#     else:
#         answer += (num_list[i]*num_list[i+1])
# if num_list[N-1] < 0 and N%2 != 0:
#     answer += num_list[N-1]
#
# print(answer)


## Second Approach
positive_l = []
negative_l = []
one_l = []

for n in num_list:
    if n > 0:
        if n == 1:
            one_l.append(1)
        else:
            positive_l.append(n)

    else:
        negative_l.append(n)

for i in range(0, len(negative_l)-1, 2):
    answer += negative_l[i]*negative_l[i+1]

if len(negative_l)%2 !=0:
    answer += negative_l[-1]


for i in range(len(positive_l)-1, 0, -2):
    answer += positive_l[i]*positive_l[i-1]

if len(positive_l)%2 !=0:
    answer += positive_l[0]

answer += sum(one_l)
print(answer)