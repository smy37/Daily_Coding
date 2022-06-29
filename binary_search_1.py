import math


def solution(distance, rocks, n):
    if len(rocks) == n:
        return distance
    rocks = sorted(rocks)
    rocks.append(distance)
    lower = 0
    upper = distance
    cri = math.ceil((upper + lower) / 2)
    cnt = 0
    answer = 0
    while 1:
        cnt = 0
        temp = [0]
        for i in range(len(rocks)):
            if rocks[i] - temp[-1] < cri:
                cnt += 1
            else:
                temp.append(rocks[i])
        # if distance-rocks[-1] < cri:
        #     cnt +=1
        # elif rocks[-1]-temp[-1] <cri:
        #     cnt +=1
        print(upper, lower, cri, cnt)
        if cnt == n:
            if cri > answer:
                answer = cri
        if cnt <= n:
            if cri > answer:
                answer = cri
            lower = cri
            cri = math.ceil((lower + upper) / 2)
            if upper == cri:
                break
        elif cnt > n:
            upper = cri
            cri = math.ceil((lower + upper) / 2)
            if upper == cri:
                break

    return answer