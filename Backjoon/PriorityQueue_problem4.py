import sys
import heapq
import math

iter= int(sys.stdin.readline())

heap = []


for i in range(iter):
    temp = int(sys.stdin.readline())
    heap.append(temp)
    heap = sorted(heap)
    cri = math.ceil(len(heap)/2)-1
    print(heap[cri])