import sys

iter_num = int(sys.stdin.readline())


for i in range(iter_num):
    temp = sys.stdin.readline().rstrip()
    fow_list = []
    sensor = True

    for j in temp:
        if j == '(':
            fow_list.append('(')
        elif j == ')' and len(fow_list) !=0:
            fow_list.pop()
        elif j == ')' and len(fow_list) == 0:
            print('NO')
            sensor = False
            break

    if sensor:
        if len(fow_list) == 0:
            print('YES')
        else:
            print('NO')
