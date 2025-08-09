import sys

N = int(sys.stdin.readline())
cri = 1%N
answer = 1

if str(N)[-1] in ["2", "4", "5", "6", "8", "0"]:
    print(-1)
    sys.exit()

while cri != 0:
    cri = ((cri*10)+1)%N
    answer += 1

print(answer)

explain = """
1 -> 11 -> 111 -> ... 이런식으로 1의 숫자를 늘려가며 N으로 나누어 떨어지는 경우에 대하여 체크를 해준다.
이때, 1->11->111 로 갈 때, 이전 수에서 *10을 해주고 +1 을 해주면 된다. 따라서 %N 연산을 적용한 나머지에다가
*10을 해주고 +1을 해줘서 나누어 떨어지는지 확인하며 된다.
"""