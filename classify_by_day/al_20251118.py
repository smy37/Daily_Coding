import sys

answer = 0

N, M = map(int, sys.stdin.readline().split())
spend_time = list(map(int, sys.stdin.readline().split()))
spend_time.sort()
memory = [0]*M

while spend_time:
    cur = min(memory)

    for i in range(M):
        memory[i] -= cur
    answer += cur
    for i in range(M):
        if memory[i] == 0 and len(spend_time) > 0:
            t = spend_time.pop()
            memory[i] = t

print(answer+max(memory))

explain = """
시간이 가장 긴 것 부터 작업을 수행하면 정답을 구할 수 있다. 시간의 리스트는 스택에 넣고 정렬해둔다.
"""