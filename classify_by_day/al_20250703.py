import sys 
import math
from collections import deque

def check_connect(n1, n2):
    cnt = 0
    for i in range(4):
        if str(n1)[i] == str(n2)[i]:
            cnt +=1

    if cnt == 3:
        return True
    else: 
        return False

def check_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

prime_l = []
prime_graph = {}
for i in range(1000, 10000):
    if check_prime(i):
        prime_l.append(i)
        prime_graph[i] =[]

for i in range(len(prime_l)):
    for j in range(i+1, len(prime_l)):
        if check_connect(prime_l[i], prime_l[j]):
            prime_graph[prime_l[i]].append(prime_l[j])
            prime_graph[prime_l[j]].append(prime_l[i])

T = int(sys.stdin.readline())


for _ in range(T):

    origin, target = map(int, sys.stdin.readline().split())
    visit = {origin: 1}
    flag = False
    dq = deque()
    dq.append([origin, 0])

    while dq:
        t, dist = dq.popleft()
        if t == target:
            print(dist)
            flag = True
            break
        for next_n in prime_graph[t]:
            if next_n not in visit:
                visit[next_n] = 1
                dq.append([next_n, dist+1])

    if not flag:
        print("Impossible")


explain = """
4자리 소수를 모두 찾고 한자리만 바꿔서 다른 소수가 될 수 있는 소수 끼리 엣지로 연결한다. 
그 후에 시작 소수로부터 타겟 소수까지 도달 할 수 있는지 BFS로 찾고 도달했을 경우, 경로의 
길이를 출력해준다.
"""