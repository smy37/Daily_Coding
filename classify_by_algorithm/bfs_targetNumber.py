import sys

final_cnt = 0
def solution(numbers, target):
    global number
    number = numbers

    f_cnt = []
    dfs([], 0, target, f_cnt)
    answer = sum(f_cnt)
    print(answer)
    return answer



def dfs(cur_number, idx, target, f_cnt):

    if idx == len(number):
        if sum(cur_number) == target:
            f_cnt.append(1)
            return
        else:
            return
    else:
        dfs(cur_number+[number[idx]], idx+1, target, f_cnt)

        dfs(cur_number+[number[idx]*-1], idx+1, target, f_cnt)
    return f_cnt

solution([4, 1, 2, 1], 2)