import sys

N = int(sys.stdin.readline())
num_l = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(0)
    sys.exit()

d_f = [0, 0, 0, 1, 1, 1, -1,-1, -1]
d_b = [0, 1, -1, 0, 1, -1, 0, 1, -1]

answer = -1
for i in range(9):
    front_num = num_l[0] + d_f[i]
    back_num = num_l[1] + d_b[i]
    temp_answer = abs(d_f[i]) + abs(d_b[i])
    flag = True

    dist = back_num-front_num
    front_num = back_num
    back_num = back_num+dist
    for j in range(2, N):
        if num_l[j] == back_num:
            back_num = back_num + dist
        elif num_l[j] - back_num == 1:
            back_num = back_num + dist
            temp_answer += 1
        elif num_l[j] - back_num == -1:
            back_num = back_num + dist
            temp_answer += 1
        else:
            temp_answer = -1
            flag = False
            break
    if flag:
        if answer == -1:
            answer = temp_answer
        else:
            answer = min(answer, temp_answer)
        answer = min(answer, temp_answer)

print(answer)

explain = """
핵심이 되는 로직은 첫번째와 두번째 수를 9가지의 경우의 수로 미리 세팅을 해서 등차를 구한후 
그 다음 수부터 해당하는 등차로 플러스 마이너스 1 사이에서 만들 수 있는지 판단하고 만약 등차 수열이 가능하다면
연산이 몇번 필요한지 카운트 해준다. 또한 N이 1일 때도 체크해줘야 한다. 
"""