import sys
import heapq
import math

iter= int(sys.stdin.readline())

heap1 = []
heap2 = []

for i in range(iter):
    temp = int(sys.stdin.readline())
    if len(heap1) == len(heap2):
        heapq.heappush(heap1, -temp)
    else:
        heapq.heappush(heap2, temp)
    if len(heap2)!=0 and -heap1[0] > heap2[0]:
        temp1 = heapq.heappop(heap1)
        temp2 = heapq.heappop(heap2)
        heapq.heappush(heap1, -temp2)
        heapq.heappush(heap2, -temp1)

    print(-heap1[0])
