import sys
import copy

N = int(sys.stdin.readline())
egg_l = []
visited = {i: 0 for i in range(N)}

for _ in range(N):
    dura, weight = map(int, sys.stdin.readline().split())
    egg_l.append([dura, weight])


def dfs(cur_idx, e_l, visit):
    for i in visit:
        if visit[i] == 0:
            n_d = e_l[cur_idx][0]-e_l[i][1]
            n_e_l = copy.deepcopy(e_l)
            n_e_l[i][0] -= e_l[cur_idx][1]

            if n_e_l[i][0] <= 0:
                visit[i] = 1

            if n_d >0:
                dfs(cur_idx, n_e_l, visit)
            else:
                for j in visit:
                    if visit[j] == 0:
                        dfs(j, n_e_l, visit)
                        break

            visit[i] = 0