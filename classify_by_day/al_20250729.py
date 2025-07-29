import sys
import heapq

answer = 0
cur = 0
N, M = map(int, sys.stdin.readline().split())
x_list = list(map(int, sys.stdin.readline().split()))

hq = []
heapq.heapify(hq)

for x in x_list:
    heapq.heappush(hq, -x)
    if cur + x>= M:
        max_elem = - heapq.heappop(hq)
        if x != max_elem:
            cur -= (2*max_elem-x)
        else:
            cur -= max_elem
        answer +=1
    else:
        cur += x
print(answer)

explain = """
현재 값이 제한선을 넘었다면 heap을 사용해서 현재 상황에서 가장 큰값을 찾고 그 값을
누적값에서 빼주는 방식으로 풀이가 가능하다. 하나 조심해줘야 할 것은 빼주는 값이 이전에
추가된 값이라면 *2를 해서 빼줘야 한다.(마이너스의 효과를 발휘하므로)
"""