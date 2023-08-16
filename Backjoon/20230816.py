import sys

n = int(sys.stdin.readline())
limit = 1000001
table = [[limit, []] for _ in range(n+1)]
table[1][0] = 0
table[1][1].append(1)
for i in range(1,n):
    if i*3 <= n and table[i*3][0] > table[i][0] + 1:
        table[i * 3][0] = table[i][0] + 1
        table[i * 3][1] = [i*3] + table[i][1]
    if i*2 <= n and table[i*2][0] > table[i][0] + 1:
        table[i * 2][0] = table[i][0] + 1
        table[i * 2][1] = [i * 2] + table[i][1]
    if i+1 <= n and table[i+1][0] > table[i][0] + 1:
        table[i + 1][0] = table[i][0] + 1
        table[i + 1][1] = [i + 1] + table[i][1]

print(table[n][0])
for i in table[n][1]:
    print(i, end= ' ')

### Dynamic Programming 말고도 BFS 또는 DFS 로도 풀어보자!!! ###