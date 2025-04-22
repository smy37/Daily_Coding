import sys
import heapq


iter = int(sys.stdin.readline())
heap = []




for i in range(iter):
    temp = int(sys.stdin.readline())

    if temp != 0 :
        heapq.heappush(heap, (abs(temp), temp))

    else:
        if len(heap) == 0:
            print(0)
        else:

            print(heapq.heappop(heap)[1])
