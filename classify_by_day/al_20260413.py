import sys
import heapq

N = int(sys.stdin.readline())
num_list = []
for _ in range(N):
    a,b = map(int, sys.stdin.readline().split())
    num_list.append([a,b])


## First Approach
num_list.sort(key= lambda x : [x[0], x[1]])
answer = 0
memory = []
heapq.heapify(memory)

for s, e in num_list:

    while len(memory) >0 and s >= memory[0]:
        heapq.heappop(memory)
    heapq.heappush(memory, e)
    answer = max(answer, len(memory))



print(answer)