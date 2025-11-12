import sys
import heapq

N = int(sys.stdin.readline())
task_l = []
memory = []
heapq.heapify(memory)
for _ in range(N):
    num, start_time, end_time = map(int, sys.stdin.readline().split())
    task_l.append([start_time, end_time])
task_l.sort()