import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX_CRI = 100000
dq = deque()
dq.append([N, 0])

visited = {N: True}
while dq:
    t, cnt = dq.popleft()
    if t == K:
        print(cnt)
        sys.exit()

    if t != 0:
        cri = int((K/t)**0.5)+1

        for i in range(1, cri+1):
            temp = t*(2**i)
            if temp not in visited and temp<=MAX_CRI:
                dq.append([temp, cnt])
                visited[temp] = True

    
    m1 = t-1
    m2 = t+1

    if m1 >= 0 and m1 not in visited:
        dq.append([m1, cnt+1])
        visited[m1] = True
    if m2 <= MAX_CRI and m2 not in visited:
        dq.append([m2, cnt+1])
        visited[m2] = True


explain = """
문제 해결의 핵심 포인트는 다음과 같다. 이동의 종류가 3가지이고 특히, 2*x 이동은 소요되는 시간이 0이라 스택에 먼저 넣어줘야 한다. 
int((K/t)**0.5)+1을 통해서 현재 숫자가 t일때, 2*x로 도달할 수 있는 후보들을 스택에 넣어주고 그 이후, t+1과 t-1에 대한 경우의 수를 스택에 추가해준다.
또한 K가 100000보다 작거나 같기 때문에, 스택에 추가하는 새로운 수의 상한이 100000이 된다. 예를들어, 100001 이라면, 100000에서 +1을 해서 이미 상한값을 지났고
100002라면 50001에서 *2를 통해 온거라면 500001에서 -1로 이동후 *2를 해주는 것이 더 소요시간이 적다. 즉, 100000 이후의 숫자라면 *2를 통해 온것이 아니라면 +1 이동으로
이미 상한이 100000을 지난 것이고 *2 이동을 통해 온것이라면 곱하기 이전에 -1 이동으로 50000으로 이동후 *2를 하는것이 무조건 이동 소요시간이 적게된다.
"""
