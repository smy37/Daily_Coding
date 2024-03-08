import sys
import heapq
N = int(sys.stdin.readline())
time_t = []

for i in range(N):
    t = list(map(int, sys.stdin.readline().split()))
    time_t.append(t)

time_t = sorted(time_t, key = lambda x : x[0])

q = []
heapq.heappush(q, time_t[0][1])

answer = 0

for i in range(1, len(time_t)):
    if len(q) == 0:
        heapq.heappush(q, time_t[i][1])
    else:
        flag = True
        while flag:
            t = q[0]
            # print('test', t, time_t[i]
            if t > time_t[i][0]:
                heapq.heappush(q, time_t[i][1])
                flag = False
            else:

                heapq.heappop(q)
    # print(time_t[i], q)
    answer = max(answer, len(q))
print(answer)