import sys
import heapq
iter = int(sys.stdin.readline())

heap = []

def heap_sort(heap_list):
    start = len(heap_list)-1
    parent = (start-1)//2

    while parent >=0:
        if heap_list[start] > heap_list[parent]:
            heap_list[start], heap_list[parent] = heap_list[parent], heap_list[start]
            start = parent
            parent = (parent-1)//2
        else:
            break

    return heap_list

for i in range(iter):
    temp = int(sys.stdin.readline())

    if temp != 0:

        heapq.heappush(heap, -temp)

    else:
        if len(heap) == 0:
            print(0)

        else:
            print(-heapq.heappop(heap))

