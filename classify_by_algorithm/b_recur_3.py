import sys

data = int(sys.stdin.readline())

def starpoint(n : int):
    if n == 1:
        temp = ''
        for i in range(3**n):
            for j in range(3**n):
                if i != 1:
                    temp += '*'
                elif i == 1:
                    if j != 1:
                        temp += '*'
                    elif j == 1:
                        temp += ' '
            if i != 2:
                temp += '\n'
        return temp

    else:

        temp_2 = starpoint(n//3).rstrip().split('\n')
        temp = ''
        for i in range(3):
            for j in temp_2:
                if i!=1:
                    temp += j*3
                    temp += '\n'
                elif i == 1:
                    temp += j + ' '*len(j) + j
                    temp += '\n'

        return temp


print(starpoint(data//3))