import sys

cri = 1000000000
dp = [0, 1]
while 1:
    temp = dp[-1] + dp[-2]
    if temp > cri:
        break
    dp.append(temp)

T = int(sys.stdin.readline())
for _ in range(T):
    temp = []
    n = int(sys.stdin.readline())
    cur = n
    for i in range(len(dp)-1, -1, -1):
        if cur <= 0:
            break
        if dp[i] <= cur:
            temp.append(dp[i])
            cur -= dp[i]

    for i in range(len(temp)-1, -1, -1):
        print(temp[i], end=" ")


explain = """
최대 n이 가질 수 있는 범위 내의 피보나치 수를 구한다음에 큰 수부터, 현재 수 이하일 경우 
해당 피보나치 수를 배열에 추가하고 해당 수만큼 현재 수에서 빼줘 현재 수를 업데이트 한다. 
이는 피보나치 수 자체가 그 다음 피보나치 수 이전의 모든 값을 그 이전 값을 통해서 만들 수 있으므로
이러한 그리디 방식이 가능하다. 
"""