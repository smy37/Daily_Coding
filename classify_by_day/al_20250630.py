import sys

## First Approach
# while 1:
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#
#     cur_str = sys.stdin.readline().strip()
#     answer = 0
#     for i in range(len(cur_str)):
#         temp = {}
#         add_idx = 0
#         while len(temp) <= n and i + add_idx < len(cur_str):
#             temp[cur_str[i + add_idx]] = 1
#             add_idx += 1
#
#         answer = max(answer, add_idx - 1)
#     print(answer)

## Second Approach -> using sliding window
while 1:
    t_answer = 0

    n = int(sys.stdin.readline())
    if n == 0:
        break
    cur_str = sys.stdin.readline().strip()

    left = 0
    specific_str = {}
    str_cnt = 0

    for right in range(len(cur_str)):
        if cur_str[right] not in specific_str:
            specific_str[cur_str[right]] = 0
            str_cnt += 1
        else:
            if specific_str[cur_str[right]] == 0:
                str_cnt += 1
        specific_str[cur_str[right]] += 1

        while str_cnt > n:
            specific_str[cur_str[left]] -= 1

            if specific_str[cur_str[left]] == 0:
                str_cnt -= 1

            left += 1

        t_answer = max(t_answer, right-left+1)


    print(t_answer)


explain = """
처음 시도에서는 시작점을 문자열 길이 만큼 지정하고 각각의 시작점에 대하여 최대 끝점을 찾는 방식을 시도하였지만
시간 초과가 발생하였다. 두번째 접근법으로 끝점을 한칸씩 늘리면서 그에 대응하는 가장 왼쪽에 있는 시작점을 찾는 슬라이딩 윈도우
방식을 사용하였다. 하나 주의해야 할점은 이전에 나왔던 문자라서 이미 specific_str에 key로 들어가 있는 경우에 대한 처리를 
신경 써야 한다.
"""