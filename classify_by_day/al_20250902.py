import sys

N = int(sys.stdin.readline())

### 1. First Approach
# answer = 1

# for i in range(N-1, 1, -1):
#     answer *= i

# answer = ((N)**(N-1)) / answer
# print(answer)

### 2. Second Approach
answer = 0

for i in range(N, -0, -1):
    answer += N/i

if N == 1:
    print(1)
else:
    print(answer)


explain = """
전체 꽃의 개수가 N이고 현재까지 뽑은 꽃의 개수가 K개라면 다음 번에서 지금까지 뽑은
꽃이 아닌 꽃을 뽑을 확률은 (N-K)/N 이고 기하 분포이므로 기대값은 역수인 N/(N-K)이다.
처음에는 누적해서 곱하는 것으로 접근했지만 기대값의 선형성에 의해 두번째 접근방법처럼
누적해서 더하는 것이 올바르다.
"""