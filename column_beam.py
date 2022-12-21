def solution(n, build_frame):
    answer = []
    frame = []
    for i in range(n + 1):
        temp = []
        for j in range(n + 1):
            temp.append([0, 0])
        frame.append(temp)

    for cmd in build_frame:
        x = cmd[0]
        y = cmd[1]
        if cmd[3] == 1:  # 설치
            if cmd[2] == 0:  # 기둥
                if y == n:
                    continue
                if y == 0 or frame[x][y - 1][0] == 1 or (x != 0 and frame[x - 1][y][1] == 1) or (
                        x != n and frame[x][y][1] == 1):
                    frame[x][y][0] = 1
                    answer.append([x, y, 0])

            elif cmd[2] == 1:  # 보
                if x == n or y == 0:
                    continue
                if frame[x][y - 1][0] == 1 or frame[x + 1][y - 1][0] == 1 or (
                        x != 0 and frame[x - 1][y][1] == 1 and frame[x + 1][y][1] == 1):
                    frame[x][y][1] = 1
                    answer.append([x, y, 1])
        elif cmd[3] == 0:  # 삭제
            if cmd[2] == 0:  # 기둥
                if y != n and frame[x][y + 1][0] == 1:  # 삭제하려는 기둥위에 기둥이 있는 경우
                    if (x == n or frame[x][y + 1][1] == 0) and (x == 0 or frame[x - 1][y + 1][1] == 0):
                        continue
                if x != 0 and frame[x - 1][y+1][1] == 1:  # 삭제하려는 기둥 왼쪽에 보가 있는 경우
                    if frame[x - 1][y][0] == 0 and (
                            x - 1 == 0 or frame[x - 2][y+1][1] == 0 or frame[x][y+1][1] == 0) == False:
                        continue
                if x != n and frame[x][y+1][1] == 1:  # 삭제하려는 기둥 오른쪽에 보가 있는 경우
                    if frame[x + 1][y][0] == 0 and (
                            x == 0 or frame[x - 1][y+1][1] == 0 or x + 1 == n or frame[x + 1][y+1][1] == 0) == False:
                        continue
                answer.remove([x, y, 0])
                frame[x][y][0] = 0
            elif cmd[2] == 1:  # 보
                if frame[x][y][0] == 1:  # 삭제하려는 보 왼쪽에 기둥이 있는 경우
                    if frame[x][y - 1][0] == 0 and (x == 0 or frame[x - 1][y][1] == 0):
                        continue
                if x != n and frame[x + 1][y][0] == 1:  # 삭제하려는 보 오른쪽에 기둥이 있는 경우
                    if frame[x + 1][y - 1][0] == 0 and frame[x + 1][y][1] == 0:
                        continue
                if x != 0 and frame[x - 1][y][1] == 1:  # 삭제하려는 보 왼쪽에 보가 있는 경우
                    if frame[x - 1][y - 1][0] == 0 and frame[x][y - 1][0] == 0:
                        continue
                if x != n and frame[x + 1][y][1] == 1:  # 삭제하려는 보 오른쪽에 보가 있는 경우
                    if frame[x + 1][y - 1][0] == 0 and (x + 1 == n or frame[x + 2][y - 1][0] == 0):
                        continue
                answer.remove([x, y, 1])
                frame[x][y][1] = 0

    answer = sorted(answer, key=lambda x: [x[0], x[1], x[2]])
    return answer