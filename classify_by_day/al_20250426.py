import sys

N = int(sys.stdin.readline())

graph = {}

for i in range(N):
    graph[i+1] = int(sys.stdin.readline())

### Method 1. 표에서 위의 값들을 담는 딕셔너리 한개와 아래 값들을 담는 스택 한개 사용 (정답 코드임)
# answer = {}
#
# for i in range(N):
#     if i + 1 not in answer:
#         temp = {i+1 : False}
#         s = [graph[i+1]]
#
#         while s:
#             t = s.pop()
#             temp[t] = True
#             if t not in temp:
#                 s.append(graph[t])
#         for t in temp:
#             if temp[t] == False:
#                 break
#         else:
#             for t in temp:
#                 answer[t] = True
#
# print(len(answer))
# answer_l = sorted(answer.keys())
# for i in answer_l:
#     print(i)

### Method 2. 시작 하는 인덱스 이외에는 연결해서 진행할 때, 자동으로 위 아래 값이 들어가므로 아래 값들을 모은 집합에 시작값이 있다면 맞는 시행임을 이용 (맞는 코드)
answer = {}
for i in range(1, N+1):
    if i not in answer:
        start = i
        bottom_v = {}
        s = [graph[i]]
        while s:
            t = s.pop()
            if graph[t] not in bottom_v:
                bottom_v[graph[t]] = True
                s.append(graph[t])
        if start in bottom_v:
            for k in bottom_v:
                answer[k] = True
print(len(answer))
for i in sorted(answer.keys()):
    print(i)

## 표에서 위의 값과 아래값을 따로 담는 배열을 이용 하는 것이 첫번째 방법
## 시작하는 숫자의 인덱스 외의 다음 값 부터는 자동으로 윗배열과 아래배열에 자동으로 담기므로 아래 값을 담긴 배열에 처번째 숫자의 인덱스가 포함되는지만 체크하면 되는 점을
## 이용한 것이 두번째 방법이다. 결국 핵심은 첫번째 시작하는 숫자의 인덱스 값이 플로우 진행이 끝나 후에 아랫값을 모은 배열에 담겨 있으면 해당 수행은 맞는 수행.