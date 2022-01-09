import sys

num, capa = map(int, sys.stdin.readline().rstrip().split())
object_list = []

for i in range(num):
    object_list.append(list(map(int, sys.stdin.readline().rstrip().split())))


test = {}
for i in range(capa):
    test[i+1] = 0

for i in object_list:
    temp = dict(test)
    for j in range(1, capa+1):
        if j+ i[0] <= capa and temp[j]!=0:
            test[j+i[0]] = max(temp[j+i[0]], temp[j] + i[1])
    if i[0] <=capa:
        test[i[0]] = max(i[1], test[i[0]])

print(max(test.values()))

print()
print('##########################################')
print()
n, k = map(int, input().split())

thing = [[0,0]]
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

print(d[n][k])