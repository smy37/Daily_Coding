import copy
import sys
sys.setrecursionlimit(10**5)
from collections import deque

N, e, w, s, n = map(int, sys.stdin.readline().split())
ep, wp, sp, np = e/100, w/100, s/100, n/100

move = [[1, 0], [-1, 0], [0, -1], [0, 1]]
move_p = [ep, wp, sp, np]
s = deque()
s.append([1, [0, 0], 0])
visited = {(0,0): True}

answer = 0

def dfs(x, y, depth, prob):
    global answer
    if depth == N:
        answer += prob
        return
    for i in range(4):
        nx, ny = x + move[i][0], y + move[i][1]
        if (nx, ny) not in visited or visited[(nx, ny)] == False:
            visited[(nx, ny)] = True
            dfs(nx, ny, depth+1, prob*move_p[i])
            visited[(nx, ny)] = False

dfs(0,0,0, 1)
print(answer)