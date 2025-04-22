from collections import deque


test = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]

def solution(operations):
    answer = []
    que = []

    for i in operations:
        temp = i.split(' ')
        cmd = temp[0]
        num = int(temp[1])

        if cmd == 'I':
           sensor = False
           if len(que) == 0:
               que.append(num)
           else:
               for j in range(len(que)):
                   if que[j] >= num:
                       que = que[:j] + [num] + que[j:]
                       sensor = True
                       break
                   else:
                       continue
               if sensor == False:
                   que.append(num)
        elif cmd == 'D':
            if num == -1:
                if len(que) ==1:
                    que = []
                elif len(que) > 1:
                    que = que[1:]
            elif num == 1:
                try :
                    que.pop()
                except:
                    que = []

    if len(que) == 0:
        answer = [0,0]
    elif len(que) == 1:
        answer = [que[0], que[0]]
    else:
        answer = [max(que), min(que)]
    print(answer)
    return answer

solution(test)