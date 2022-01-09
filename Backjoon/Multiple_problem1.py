import sys

sensor = True

while sensor:
    temp = list(map(int,sys.stdin.readline().rstrip().split()))
    if temp[0] == 0 and temp[1] == 0:
        sensor = False
        break
    elif temp[1]%temp[0] == 0 and temp[1]//temp[0] > 1:
        print('factor')
    elif temp[0]%temp[1] == 0 and temp[0]//temp[1] > 1:
        print('multiple')
    else:
        print('neither')


