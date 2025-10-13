import sys 

def dp(num_l: list, N, S, T):
    answer = -float("inf")
    memory = [[-float("inf") for _ in range(N+2)] for _ in range(T)]
    for i in range(1,S+1):
        memory[0][i] = max(memory[0][i], num_l[i-1])
    for i in range(1, T):
        for j in range(N+2):
            if memory[i-1][j] != -float("inf"):
                for s in range(1, S+1):
                    if j+s >= N+1:
                        memory[i][N+1] = max(memory[i][N+1], memory[i-1][j])
                    else:
                        memory[i][j+s] =\
                            max(memory[i][j+s], memory[i-1][j]+num_l[j+s-1])
        answer = max(answer, memory[i][N+1])

    return answer

N, S, T = map(int, sys.stdin.readline().split())
total_num = []
while 1:
    cur_l = list(map(int, sys.stdin.readline().split()))

    if len(cur_l) == 1 and cur_l[0] == 0:
        break
    else:
        if len(total_num) >= N:
            print(dp(total_num, N, S, T))
            N, S, T = cur_l
            total_num = []
        else:
            total_num.extend(cur_l)
print(dp(total_num, N, S, T))

explain = """
T개의 단계동안 주사위를 던질 때, 각 단계별로 발판과 최대값을 저장해 둔다.
T동안 이전 단계에서의 발판에서 1~S만큼 움직여서 현재 발판을 업데이트 해준다.
"""