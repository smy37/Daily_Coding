import sys 
from collections import deque
N, M = map(int, sys.stdin.readline().split())
on_off_l = {}
for _ in range(M):
	x, y, a, b = map(int, sys.stdin.readline().split())
	if (x,y) not in on_off_l:
		on_off_l[(x,y)] = []
	on_off_l[(x,y)].append((a,b))

s = deque([[1,1]])
enable_in = {(1,1):True}
visited = {}

visited[(1,1)] = True
dx = [0,0,-1,1]
dy = [1,-1,0,0]

while s:
	c_x, c_y = s.popleft()
	
	if (c_x, c_y) in on_off_l:
		for o_x, o_y in on_off_l[(c_x,c_y)]:
			if (o_x, o_y) not in enable_in:
				enable_in[(o_x, o_y)] = True

				for i in range(4):
					n_x = o_x + dx[i]
					n_y = o_y + dy[i]
					if (n_x, n_y) in visited:
						s.append([o_x, o_y])
						visited[(o_x,o_y)] = True
						break
	for i in range(4):
		n_x = c_x + dx[i]
		n_y = c_y + dy[i]
		if 1<= n_x <= N and 1<= n_y <= N:
			if (n_x, n_y) in enable_in and (n_x, n_y) not in visited:
				s.append([n_x, n_y])
				visited[(n_x, n_y)] = True

print(len(enable_in))