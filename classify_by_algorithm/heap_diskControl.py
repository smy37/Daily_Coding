import sys
import heapq



jobs = 	 [[0, 5], [2, 10], [100000000000, 2]]
def solution(jobs):
    answer = 0
    length = len(jobs)
    for i in range(len(jobs)):
        jobs[i] = [jobs[i][1], jobs[i][0]]
    jobs = sorted(jobs, key=lambda x: [x[1], x[0]])
    total, cur = 0,0
    cur += jobs[0][1]
    total += cur + jobs[0][0] - jobs[0][1]
    cur += jobs[0][0]
    jobs.remove(jobs[0])
    while jobs:
        heap = []
        flg1 = False
        for i in range(len(jobs)):
            if jobs[i][1] <= cur:
                heapq.heappush(heap, jobs[i])
                flg1 = True


        if flg1:
            temp = heapq.heappop(heap)
            jobs.remove(temp)
            total += cur - temp[1] + temp[0]
            cur += temp[0]
        else:
            cur = jobs[0][1]
    answer = int(total/length)
    print(answer)
    return answer

solution(jobs)