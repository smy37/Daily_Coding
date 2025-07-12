import sys
import heapq

T = int(sys.stdin.readline())

### First Approach
# for _ in range(T):
#     k = int(sys.stdin.readline())
#     min_heap = []
#     max_heap = []
#     heapq.heapify(min_heap)
#     heapq.heapify(max_heap)
#     max_pop_cnt = 0
#     min_pop_cnt = 0
#     cnt = 0
#     for _ in range(k):
#         cmd, num = sys.stdin.readline().split()
#         num = int(num)
#
#         if cmd == "I":
#             cnt += 1
#             heapq.heappush(min_heap, num)
#             heapq.heappush(max_heap, -num)
#         elif cmd == "D":
#             if cnt == 0:
#                 continue
#             if num == 1:
#                 heapq.heappop(max_heap)
#                 max_pop_cnt += 1
#             elif num == -1:
#                 heapq.heappop(min_heap)
#                 min_pop_cnt += 1
#
#             if max_pop_cnt + min_pop_cnt == cnt:
#                 min_heap = []
#                 max_heap = []
#                 heapq.heapify(min_heap)
#                 heapq.heapify(max_heap)
#                 max_pop_cnt = 0
#                 min_pop_cnt = 0
#                 cnt = 0
#
#     if cnt == 0:
#         print("EMPTY")
#     else:
#         max_v = -heapq.heappop(max_heap)
#         min_v = heapq.heappop(min_heap)
#         print(max_v, min_v)


### Second Approach
for _ in range(T):
    k = int(sys.stdin.readline())
    min_heap = []
    max_heap = []
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    visited = {}

    for i in range(k):
        cmd, num = sys.stdin.readline().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(min_heap, [num, i])
            heapq.heappush(max_heap, [-num, i])
            visited[i] = True
        elif cmd == "D":

            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])

explain = """
첫번째 시도에서는 최대힙과 최소힙을 구성해서 최대힙에서 pop되는 개수와 최소힙에서 pop되는 개수를 기록한 후에 그 개술르 기반으로 
최종 출력을 도출하는 방법이었다. 그러나 이 방법은 한쪽 힙에서 제거된게 다른 힙의 뒤에서 암묵적으로 제거되고 다른 힙에서 앞에서부터 
pop되어 암묵적으로 제거된 부분앞까지 온다면 잘못된 답을 도출하게 된다. 
따라서, 한쪽 힙에서 제거될때, 그 인덱스를 기록해뒀다가 다른 힙에서 해당 인덱스의 값들을 제거하는 식으로 동작해서 암묵적으로 지워진
부분을 실제로 지워서 해결한다.
"""