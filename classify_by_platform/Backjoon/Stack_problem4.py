import sys


while 1:
    s1 = []

    temp = sys.stdin.readline().rstrip()
    if temp == '.':
        sys.exit()
    else:
        sensor = True
        for i in temp:
            if i == '(':
                s1.append(i)
            elif i == '[':
                s1.append(i)

            elif i == ')' and len(s1)!= 0 and s1[-1] == '(':
                s1.pop()
            elif i == ']' and len(s1)!= 0 and s1[-1] == '[':
                s1.pop()
            elif i == ')' and len(s1)!= 0 and s1[-1] != '(':
                print('no')
                sensor = False
                break
            elif i == ']' and len(s1)!= 0 and s1[-1] != '[':
                print('no')
                sensor = False
                break
            elif (i == ')' or i == ']') and len(s1) == 0:
                print('no')
                sensor = False
                break



        if sensor:
            if len(s1) ==0:
                print('yes')
            else:
                print('no')
