import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp_dec = [0 for _ in range(N)]
dp_inc = [0 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            dp_dec[i] = max(dp_dec[i], dp_dec[j]+1)
for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[j] > arr[i]:
            dp_inc[i] = max(dp_inc[i], dp_inc[j]+1)

answer = 0
for i in range(N):
    if answer < dp_inc[i] + dp_dec[i]:
        answer = dp_inc[i]+dp_dec[i]

print(answer+1)

explain = """
왼쪽에서 오른쪽으로 가면서 감소하는 수열의 길이를 저장해두어 업데이트 과정과 오른쪽에서 왼쪽으로 가면서 
증가하는 수열의 길이를 저장하고 업데이트 하는 과정 모두 필요하였다.
그리고 마지막으로 O(N)의 시간복잡도를 지닌 감소하는 수열과 증가하는 수열의 합을 통해 가장 긴 수열을 찾는 과정이 존재한다.
"""