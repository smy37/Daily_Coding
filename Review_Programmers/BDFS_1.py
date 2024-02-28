import sys

def bfs(cur_num, cur_idx, target, nl):
    if cur_idx == len(nl):
        if cur_num == target:
            return 1
        else:
            return 0
    else:
        answer = bfs(cur_num+nl[cur_idx], cur_idx+1, target, nl) + bfs(cur_num-nl[cur_idx], cur_idx+1, target, nl)
        return answer
def solution(numbers, target):
    answer = 0
    answer = bfs(0, 0, target, numbers)
    return answer

if __name__ == "__main__":
    n_l = [1, 1, 1, 1, 1]
    target = 3
    print(solution(n_l, target))