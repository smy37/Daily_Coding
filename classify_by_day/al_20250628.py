import sys 

N = int(sys.stdin.readline())
num_order = {}
str_list = []
for i in range(N):
    t = sys.stdin.readline().strip()
    num_order[t] = i+1
    str_list.append(t)

str_list.sort()
answer = 0
answer_l = []


### First Approach
# for i in range(N-1):
#     t = 0
#     cri_length = min(len(str_list[i]), len(str_list[i+1]))
#     for j in range(cri_length):
#         if str_list[i][j] != str_list[i+1][j]:
#             break
#         t += 1
    
#     if str_list[i] != str_list[i+1]:
#         if answer < t:
#             answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
#             answer = t
#         elif answer == t and len(answer_l) > 0:
#             past_max, past_min = max(answer_l[0][1], answer_l[1][1]), min(answer_l[0][1], answer_l[1][1])
#             cur_max, cur_min = max(num_order[str_list[i]], num_order[str_list[i+1]]), min(num_order[str_list[i]], num_order[str_list[i+1]])
            
#             if past_min > cur_min:
#                 answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
#                 answer = t
#             elif past_min == cur_min:
#                 if past_max > cur_max:
#                     answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
#                     answer = t
# answer_l.sort(key=lambda x: x[1])

# if len(answer_l) == 0:
#     cnt = 0
#     for k in num_order:
#         print(k)
#         cnt += 1
#         if cnt == 2:
#             break
# else:
#     for i in answer_l:
#         print(i[0])

### Second Approach -> O(n^2)
for i in range(N-1):
    t = 0
    cri_length = min(len(str_list[i]), len(str_list[i+1]))
    for j in range(cri_length):
        if str_list[i][j] != str_list[i+1][j]:
            break
        t += 1
    
    if str_list[i] != str_list[i+1]:
        if answer < t:
            answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
            answer = t
        elif answer == t and len(answer_l) > 0:
            past_max, past_min = max(answer_l[0][1], answer_l[1][1]), min(answer_l[0][1], answer_l[1][1])
            cur_max, cur_min = max(num_order[str_list[i]], num_order[str_list[i+1]]), min(num_order[str_list[i]], num_order[str_list[i+1]])
            
            if past_min > cur_min:
                answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
                answer = t
            elif past_min == cur_min:
                if past_max > cur_max:
                    answer_l = [[str_list[i], num_order[str_list[i]]], [str_list[i+1], num_order[str_list[i+1]]]]
                    answer = t
answer_l.sort(key=lambda x: x[1])

if len(answer_l) == 0:
    cnt = 0
    for k in num_order:
        print(k)
        cnt += 1
        if cnt == 2:
            break
else:
    for i in answer_l:
        print(i[0])


explain = """
첫번째 시도에서 정렬 후에 인접한 두쌍만 비교해서 답을 구하는 접근을 시도하였다. 
그러나 반례가 존재하였고 O(n^2)의 시간 복잡도를 가지도록 완전 탐색을 수행하였다.
그외에는 접두사가 존재하는 단어가 한개도 없는 엣지케이스에 대한 처리와 문제에서 요구하는
입력 순서에 따라 접두사 길이가 같은 경우에 대해 처리를 하는 로직을 추가하였다.
"""