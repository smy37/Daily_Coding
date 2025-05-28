import sys
from collections import deque
while 1:
    L, R, C = map(int, sys.stdin.readline().split())
    if [L, R, C] == [0,0,0]:
        break
    building = []
    start = [-1, -1, -1]
    end = [-1, -1, -1]
    gold = {}

    for floor in range(L):
        for row in range(R):
            t = sys.stdin.readline()
            for c in range(len(t)):
                if t[c] == "S":
                    start = [floor, row, c]
                elif t[c] == "E":
                    end = [floor, row, c]
                elif t[c] == "#":
                    gold[tuple([floor, row, c])] = 1
        skip = sys.stdin.readline()
    mv = [[1,0,0], [-1,0,0], [0,1,0], [0,-1,0], [0,0,1], [0,0,-1]]
    s = deque()
    s.append(start+[0])
    visited = {}
    flag = False
    while s:
        cur_f, cur_r, cur_c, cur_t = s.popleft()
        if [cur_f, cur_r, cur_c] == end:
            print(f"Escaped in {cur_t} minute(s)")
            flag = True
            break
        for i in range(len(mv)):
            af, ar, ac = mv[i]
            nf, nr, nc = cur_f+af, cur_r+ ar,cur_c+ac

            if 0<=nf<L and 0<=nr<R and 0<=nc<C and (nf, nr, nc) not in gold and (nf, nr, nc) not in visited:
                visited[(nf, nr, nc)] = 1
                s.append([nf, nr, nc, cur_t + 1])

    if not flag:
        print("Trapped!")
        
explain= """
BFS에서 queue에서 빠져 나오는 것은 순서대로 소요시간이 가장 짧은 것들 순서대로 나오므로 BFS를 3차원 배열에 적용하면 답을 구할 수 있다.
특정 지점에 도달 할 때, 해당 지점까지 가는 경로가 어떠하던지 해당 지점까지 가장 최단 경로로 갈 수 있다면 BFS를 통해서 구하면 된다.
반대로 특정 지점에 도달 할 때, 해당 지점까지 가는 경로가 유의미하다면 DFS와 백트래킹을 조합해서 구하면 된다.
"""