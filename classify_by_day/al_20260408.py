import sys

T, N = map(int, sys.stdin.readline().split())

constraint = {}

for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    sort_const = sorted(line[1:])
    constraint[tuple(sort_const)] = True


def checker(stack):
    for c in constraint:
        flag = True
        for n in c:
            if n not in stack:
                flag = False
                break
        if flag:
            return False
    return True


answer = 0
def find_comb(cur_idx, cur_stack):
    global answer
    if cur_idx == T:
        return
    find_comb(cur_idx+1, cur_stack)
    if checker(cur_stack+[cur_idx+1]):

        answer += 1
        find_comb(cur_idx+1, cur_stack+[cur_idx+1])

find_comb(0, [])
print(answer+1)