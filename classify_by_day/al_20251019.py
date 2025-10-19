import sys

def solution(limit_dist: int, oper_num: int, oper_dist: list[int], oper_time: list[int]):
    cmd_list = ["do_oper", "do_not_oper"]
    dp = [{"do_oper": [float("inf"), limit_dist, []], \
           "do_not_oper": [float("inf"), limit_dist, []]} for _ in range(oper_num+2)]
    for c in cmd_list:
        dp[0][c] = [0, limit_dist, []]
        dp[0][c] = [0, limit_dist, []]

    for i in range(oper_num+1):
        for cmd in cmd_list:

            cur_time, cur_rest_dist, history = dp[i][cmd]
            for idx in range(i+1, len(oper_dist)):
                next_dist = oper_dist[idx]
                if cur_rest_dist < next_dist:
                    break
                cur_rest_dist -= next_dist

                if dp[idx]["do_oper"][0] > cur_time + oper_time[idx]:
                    dp[idx]["do_oper"][0] = cur_time + oper_time[idx]
                    dp[idx]["do_oper"][1] = limit_dist
                    dp[idx]["do_oper"][2] = history + [idx]
                if dp[idx]["do_not_oper"][0] > cur_time:
                    dp[idx]["do_not_oper"][0] = cur_time
                    dp[idx]["do_not_oper"][1] = cur_rest_dist
                    dp[idx]["do_not_oper"][2] = history + [idx]

    answer = dp[-1]
    print(answer["do_oper"][0])
    print(len(answer["do_oper"][2])-1)
    for n in answer["do_oper"][2][:-1]:
        print(n, end=" ")


if __name__ == "__main__":
    l_d = int(sys.stdin.readline())
    o_n = int(sys.stdin.readline())
    o_d = [0] + list(map(int, sys.stdin.readline().split()))
    o_t = [0] + list(map(int, sys.stdin.readline().split())) + [0]

    solution(l_d, o_n, o_d, o_t)

explain = """
각 정비소 위치에서 현재 정비소에서 정비를 할경우와 정비를 하지 않을 경우에 소요시간, 남은 가용 거리, 누적 정비소를 기록해둔다. 
맨 앞에 더미를 두고 마지막에 도착지로 하고 도착지에서의 시간과 정비소 기록으로 답을 구하면 된다.
핵심은 각 정비소에서 현재 정비소를 이용할 경우와 이용하지 않을 경우를 나눠서 최소값을 업데이트 해주는 것이다.
"""

