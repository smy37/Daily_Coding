import sys
from collections import deque


iter_num = int(sys.stdin.readline())




for i in range(iter_num):
    sensor = True
    message = sys.stdin.readline().rstrip().replace('RR','')
    array_len = int(sys.stdin.readline())
    array = sys.stdin.readline().replace('[','').replace(']','').replace(',', ' ').rstrip().split(' ')
    if array == ['']:
        array = []
    rev_cnt = 0
    dq = deque(array)

    for j in message:
        if j == 'R':
            rev_cnt +=1

        elif j == 'D':
            if rev_cnt % 2 == 0:
                try:
                    dq.popleft()
                except:
                    print('error')
                    sensor = False
                    break
            elif rev_cnt % 2 == 1:
                try:
                    dq.pop()
                except:
                    print('error')
                    sensor = False
                    break

    if sensor:
        if len(dq) == 0:
            print('[]')
        else:

            if rev_cnt % 2 == 1:
                dq.reverse()
                dq = list(dq)
            else:
                dq = list(dq)
            print('[', end = '')
            for x in dq[:-1]:
                print(x, end = ',')
            print(dq[-1], end = ']\n')


