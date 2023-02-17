import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())

pq = PriorityQueue()
cnt = 0
for i in range(N):
    temp = int(sys.stdin.readline())
    pq.put(temp)

while pq.qsize()>1:
    a = pq.get()
    b = pq.get()
    cnt += (a+b)
    pq.put(a+b)


print(cnt)