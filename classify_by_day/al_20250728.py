import sys 
import heapq

N, M = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

answer = sum(a_list)

heap_comp = []
heapq.heapify(heap_comp)
for i in range(len(a_list)):
    heapq.heappush(heap_comp, [-b_list[i], 100-a_list[i]])

time_n = 24*N

while time_n > 0 and heap_comp:
    cur_item = heapq.heappop(heap_comp)
    w, rest = -cur_item[0], cur_item[1]

    a = rest // w
    b = rest % w 
    minus = min(a, time_n)
    time_n -= minus
    
    answer += minus*w
    
    if b > 0:
        heapq.heappush(heap_comp, [-b, b])

print(answer)

explain = """
현재 시간당 점수를 가장 많이 받는 항목으로 최대한 점수를 확보하고
그 나머지를 시간당 점수로 가지는 항목으로 추가해서 다시 시간당 점수를 가장
많이 받는 항목을 구한다. 이때, 최소힙을 이용한다면 빠른시간내에 업데이트 되는
상황내에서 현재 가장 점수를 많이 얻는 항목을 구할 수 있다.
"""