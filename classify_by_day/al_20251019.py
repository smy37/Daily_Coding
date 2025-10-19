import sys

def solution(limit_dist: int, oper_num: int, oper_dist: list[int], oper_time: list[int]):
    dp = [{"do_oper": [float("inf"), []], "do_not_oper": [float("inf"), []]} for _ in range(oper_num)]

    for i in range(oper_num):
        for j in range(i+1, len(oper_dist)):
            next_dist = oper_dist[j]


if __name__ == "__main__":
    l_d = int(sys.stdin.readline())
    o_n = int(sys.stdin.readline())
    o_d = list(map(int, sys.stdin.readline().split()))
    o_t = list(map(int, sys.stdin.readline().split()))

    solution(l_d, o_n, o_d, o_t)


