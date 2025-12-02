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


answer = 0

for s, e in task_l:
    if len(memory) == 0:
        heapq.heappush(memory, e)
    else:
        while 1:
            if s >= memory[0]:
                t = heapq.heappop(memory)
                if len(memory) == 0:
                    break
            else:
                break
        heapq.heappush(memory, e)
    answer = max(answer, len(memory))

print(answer)

explain = """
시작 시간을 기준으로 원소들을 정렬한다. 그리고 memory라는 힙을 하나 생성하고 시작 시간 순서대로 memory에 종료 시간을 넣어준다.
이때, 현재 시작 시간과 heap(최소힙)의 첫번째 원소를 비교후에 현재 시작 시각이 크거나 같다면 heap에 있는 원소를 없애준다. 
이러한 것을 모든 원소에 대하여 반복하고 그때 마다, memory의 크기를 체크해준다. 
"""