import sys 

answer = float("inf")
N, M = map(int, sys.stdin.readline().split())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

left = 0
if M == 0:
    print(0)
    sys.exit()

for right, n in enumerate(num_list):
    print(left, right, answer)
    while left < right:
        if n-num_list[left] < M:
            break
        else:
            answer = min(answer, n-num_list[left])
            left += 1

print(answer)