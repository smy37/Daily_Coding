import sys
import heapq

N = int(sys.stdin.readline())
max_day = 0
data = []
for i in range(N):
    f_day, score = map(int, sys.stdin.readline().split())
    max_day = max(max_day, f_day)
    data.append([f_day, score])
data = sorted(data, key = lambda x:x[0])

heap = []
cur = max_day
answer = 0

while 1:
    t = data.pop()
    if cur > t[0]:
        dur = cur - t[0]
        for i in range(dur):
            if heap:
                a = answer
                answer += abs(heapq.heappop(heap))
                b = answer

        heapq.heappush(heap, -t[1])
        cur = t[0]
    else:
        heapq.heappush(heap, -t[1])

    if len(data) == 0:
        for i in range(t[0]):
            if heap:
                a = answer
                answer += abs(heapq.heappop(heap))
                b = answer

        break

print(answer)