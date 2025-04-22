import sys

tree_height = int(sys.stdin.readline())
edge_weight = [0,0]+list(map(int, sys.stdin.readline().split()))
node_n = 2**(tree_height+1)-1
dp = [0 * (node_n+1)]


s = [1]

def dfs(s):
    t = s.pop()
    if t*2 > node_n:
        return edge_weight[t]

    n1 = t*2
    n2 = t*2+1
    l_s = dfs(s+[n1])
    r_s = dfs(s+[n2])

    acc_s = l_s
    if l_s > r_s:
        acc_s = l_s
        edge_weight[n2] += l_s-r_s
    elif l_s < r_s:
        acc_s = r_s
        edge_weight[n1] += r_s-l_s

    return acc_s + edge_weight[t]
dfs(s)
print(sum(edge_weight))