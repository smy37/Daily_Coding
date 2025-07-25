import sys

N, X = map(int, sys.stdin.readline().split())

level_num = {0: 1}
end = 1
for i in range(N):
    end = 2 * end + 3
    level_num[i + 1] = level_num[i] * 2 + 1

start = 1
answer = 0

while 1:
    mid = (start + end) // 2
    if X == start:
        break
    elif X == end:
        answer += level_num[N]
        break
    if X == mid:
        answer += (level_num[N] - 1) // 2 + 1
        break
    elif X < mid:
        start = start + 1
        end = mid - 1
    elif X > mid:
        answer += (level_num[N] - 1) // 2 + 1
        start = mid + 1
        end = end - 1
    N -= 1
    if N == 0:  ## 주의 해야 되는 부분..
        answer += 1
        break

print(answer)

explain = """
시작과 끝 인덱스를 설정해 두고 mid 값을 기준으로 왼쪽인지 오른쪽인지 판단한 후 레벨을 내려준다.
이때, 누적되는 패티의 개수를 업데이트 해준다. mid를 기준으로 왼쪽의 현재 레벨 총 패티 개수를 알 수 있으므로
mid 보다 크다면 왼쪽의 현재 레벨 총 패티 개수 만큼 더해주고 만약 mid보다 작다면 패티 개수 갱신없이 
다음 레벨로 이동한다.
주의해야 할점은 마지막에 레벨이 0이 됐는데 끝나지 않았다면 패티 개수에 1을 추가 해줘야 하는 것이다.
"""