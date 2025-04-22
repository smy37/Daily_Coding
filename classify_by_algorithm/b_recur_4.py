import sys

data = int(sys.stdin.readline())

def hanoi(n : int):
    if n == 2:
        return ['12', '13', '23']
    else:
        temp = hanoi(n-1)
        new = []
        for i in temp:
            tt = ''
            for j in i:
                if j == '2':
                    tt+= '3'
                elif j == '3':
                    tt+='2'
                else:
                    tt+= j
            new.append(tt)
        new.append('13')

        for i in temp:
            tt = ''
            for j in i:
                if j == '1':
                    tt+='2'
                elif j == '2':
                    tt+='1'
                elif j == '3':
                    tt+=j
            new.append(tt)

        return new

temp = hanoi(data)
print(len(temp))
for i in temp:
    print(i[0], i[1])
