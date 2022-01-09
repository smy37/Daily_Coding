import sys

iter_num = int(sys.stdin.readline())


result = []
cur = 0
temp_list = []
for i in range(iter_num):
    temp = int(sys.stdin.readline())
    if len(result) == 0:
        for i in range(temp):
            result.append('+')
            temp_list.append(i+1)
        result.append('-')
        cur= temp
        temp_list.pop()
    else:
        try :
            if len(temp_list) == 0 and cur < temp:
                for j in range(temp-cur):
                    result.append('+')
                    temp_list.append(cur+j+1)
                result.append('-')
                temp_list.pop()
                cur = temp
            elif temp_list[-1] == temp:
                result.append('-')
                temp_list.pop()
            elif cur < temp:
                for j in range(temp-cur):
                    temp_list.append(cur+j+1)
                    result.append('+')
                result.append('-')
                temp_list.pop()
                cur = temp
            elif temp_list[-1] != temp:
                print('NO')
                sys.exit()
        except IndexError:
            print('NO')
            sys.exit()

for i in result:
    print(i)