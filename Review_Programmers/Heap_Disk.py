import sys
import math
import heapq
from collections import deque
def solution(jobs):
    final = 0

    hq = []
    jobs = sorted(jobs)
    dq = deque([[i[1], i] for i in jobs])
    cur = 0

    while len(dq) > 0:
        temp = dq.popleft()

        if temp[1][0] <= cur:
            heapq.heappush(hq, temp)

        else:
            if len(hq) == 0:
                cur = temp[1][0]
                cur += temp[0]
                final += temp[0]

            else:
                dq.appendleft(temp)
                short_disk = heapq.heappop(hq)
                final += cur - short_disk[1][0] + short_disk[0]
                cur += short_disk[0]


    if len(hq) == 0:
        final = math.floor(final/len(jobs))
    else:
        while len(hq) > 0:
            short_disk = heapq.heappop(hq)
            final += cur - short_disk[1][0] + short_disk[0]
            cur += short_disk[0]
        final = math.floor(final/len(jobs))
    return final

q = [[0, 3], [1, 9], [2, 6]]
print(solution(q))