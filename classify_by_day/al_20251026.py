import sys 

N = int(sys.stdin.readline())

o1, o2 = map(int, sys.stdin.readline().split())

open_door = []
open_door.append([0, [o1, o2]])
L = int(sys.stdin.readline())
for _ in range(L):
    use_door = int(sys.stdin.readline())
    temp = []
    for item in open_door:
        min_open = min(item[1])
        max_open = max(item[1])

        if min_open >= use_door:
            temp.append([item[0]+min_open-use_door, [use_door, max_open]])
        elif max_open <= use_door:
            temp.append([item[0]+use_door-max_open, [min_open, use_door]])
        else:
            temp.append([item[0]+use_door-min_open, [max_open, use_door]])
            temp.append([item[0]+max_open-use_door, [min_open, use_door]])


    open_door = temp

answer = float("inf")

for item in open_door:
    answer = min(answer, item[0])

print(answer)

explain = """"
현재 단계에서 열려있는 문의 위치에 따라서 이동할 수 있는 경우의 수를 업데이트 해준 후 그 값을 바탕으로
다음 단계에서의 가능한 경우를 기록해준다.
발상은 열려있는 문과 열어야 하는 문의 위치를 빼주면 최소로 이동해야 하는 수가 나온다는 것이다.
"""