import sys 

def dp(num_l: list, N, S, T):
    memory = [[-float("inf") for _ in range(T)] for _ in range(N+2)]
    for i in range(1,S+1):
        memory[i][0] = max(memory[i][0], num_l[i-1])


N, S, T = map(int, sys.stdin.readline().split())
total_num = []
while 1:
    cur_l = list(map(int, sys.stdin.readline().split()))

    if len(cur_l) == 1 and cur_l[0] == 0:
        break
    else:
        if len(total_num) >= N:

            N, S, T = cur_l
            total_num = []
        else:
            total_num.extend(cur_l)