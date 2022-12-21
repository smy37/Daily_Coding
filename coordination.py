import math

def solution(k, d):
    answer = 0
    num_list = []
    for i in range(d//k+1):
        num_list.append(i*k)

    for i in num_list:
        answer += (int(math.sqrt(d**2 - i**2))//k+1)
    return answer


print(solution(2, 4))
cmd = [1,1,1,1]
x = cmd[0]
y = cmd[1]
n = 5
frame = []
for i in range(n + 1):
    temp = []
    for j in range(n + 1):
        temp.append([0, 0])
    frame.append(temp)
if cmd[2] == 1:  # 보
    if x == n or y == 0:
        print('err1')
    if frame[x][y - 1][0] == 1 or frame[x + 1][y - 1][0] == 1 or (
            x != 0 and frame[x - 1][y][1] == 1 and frame[x + 1][y][1] == 1):
        frame[x][y][1] = 1
        print('olleh')

for i in frame:
    print(i)