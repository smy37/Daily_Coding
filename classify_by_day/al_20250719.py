import sys

N = int(sys.stdin.readline())

buildings = []
cnt = [0 for _ in range(N)]
for _ in range(N):
    buildings.append(int(sys.stdin.readline()))

stack = []
for i in range(N-1, -1, -1):
    if len(stack) == 0:
        stack.append([buildings[i], i])
    else:
        while stack and stack[-1][0] < buildings[i]:
            cnt[i] += cnt[stack[-1][1]] + 1
            stack.pop()
        stack.append([buildings[i], i])
    
print(sum(cnt))

explain = """
stack에 높이를 뒤에서 부터 넣어가며 현재 높이보다 낮다면 스택에서 제거해준다. 
다만 주의해야 할 점은, stack에 값을 제거하더라도 왼쪽에 있는 빌딩이 제거하는 빌딩까지
본인 이상의 높이가 없다면 제거되는 빌딩도 볼 수 있으므로 따로 누적해서 값을 저장해둬야 한다.
"""
