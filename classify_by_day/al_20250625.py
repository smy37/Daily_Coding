import sys

def cal_dist(alpha):
    if alpha.isupper():
        return ord(alpha)-38
    else:
        return ord(alpha)-96

N = int(sys.stdin.readline())
limit = N
total = 0

edge_list = []

for i in range(N):
    t_str = sys.stdin.readline().strip()

    for j in range(N):
        if t_str[j] != "0":
            edge_list.append([cal_dist(t_str[j]), i+1, j+1])
            total += cal_dist(t_str[j])

edge_list.sort(key= lambda x : x[0])

parent = {i: i for i in range(1, N+1)}
def find(t):
    if t != parent[t]:
        parent[t] = find(parent[t])
    return parent[t]

def union(a, b):
    pa = find(a)
    pb = find(b)
    if pa <= pb:
        parent[pb] = pa
    else:
        parent[pa] = pb

answer = 0
flag = False if N != 1 else True
cnt = 0
for edge in edge_list:

    dist, a, b = edge
    if find(a) != find(b):
        cnt += 1
        answer += dist
        union(a,b)
        if cnt == N - 1:
            flag = True
            break


if flag:
    print(total - answer)
else:
    print(-1)

explain = """
DFS/BFS는 node의 방문에 중점을 두고 크루스칼은 사용되지 않은 Edge에 중점을 둔다. 처음에는 경로 문제인거 같아서 백트래킹으로 할려고 했지만 
node의 방문에 중점을 두는 방법이라 MST를 구하기 적합하지 않았다.
엣지케이스에 대한 처리가 어려웠었는데 flag를 True로 만들어 주는 시점과 flag 값을 N이 1일 때 따로 처리해줘야 하는 것등 
여러가지 처리가 필요하였다.
"""