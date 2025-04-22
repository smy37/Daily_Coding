import sys
import math

temp = int(sys.stdin.readline())

real_temp = str(math.factorial(temp))

cnt = 0
for i in real_temp[-1::-1]:
    if i == '0':
        cnt+=1
    else:
        break
print(cnt)