import sys

N, M = map(int, sys.stdin.readline().split())
pre = [0 for _ in range(M)]

### 1. First Try
# for _ in range(N):
#     weapon = list(map(int, sys.stdin.readline().split()))
#     temp = [float('inf') for _ in range(M)]
#     for i in range(M):
#         for j in range(M):
#             if i != j:
#                 temp[i] = min(temp[i], weapon[i] + pre[j])
#     pre = temp
# print(min(pre))

### 2. Second Try
for _ in range(N):
    weapon = list(map(int, sys.stdin.readline().split()))
    temp = [float('inf') for _ in range(M)]

    first_min = float('inf')
    second_min = float('inf')
    first_idx = -1
    for i in range(M):
        if pre[i] < first_min:
            second_min = first_min
            first_min = pre[i]
            first_idx = i

        elif pre[i] < second_min:
            second_min = pre[i]

    for i in range(M):
        if i == first_idx:
            temp[i] = second_min + weapon[i]
        else:
            temp[i] = first_min + weapon[i]

    pre = temp

print(min(pre))

explain = """
이전까지의 시간 기록을 누적해서 가지고 있다가 현재 회차의 소요 시간을 더해서 가장 최소가 되는 시간으로 업데이트 하는 핵심 아이디어는
첫번째와 두번째 모두 사용되었다. 그러나 첫번째는 가장 최소가 되는 시간을 찾기 위해서, 현재 회차의 각 무기별 소요시간과 이전 회차의 
모든 무기별 소요 시간을 비교해서 O(n^2)이 소요되었고 시간 복잡도가 너무 높았다. 그러나 생각해보면 이전 회차에서 가장 소요시간이 적게
드는 무기와 그 무기의 인덱스를 가지고 있고 두번째로 가장 소요시간이 적게 드는 것을 가지고 있다면 현재 회차의 모든 무기에서 이전 회차에서
가장 적게 소요시간이 드는 것과 같은 인덱스를 가지는 항목만 제외하고 이전 회차에서 가장 적게 드는 것과 더한 값으로 갱신해주고 나머지 한개는
두번째로 소요시간이 적게드는것과 합해서 갱신해주면 된다. 
"""