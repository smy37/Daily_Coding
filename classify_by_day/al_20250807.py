import sys
import math

X, Y = map(int, sys.stdin.readline().split())
diff = Y-X
s_diff = math.sqrt(diff)
if diff == 0:
    print(0)
else:
    if s_diff%1 == 0:
        print(2*int(s_diff)-1)
    else:
        duplicate = diff - int(s_diff)**2

        if duplicate <= s_diff:
            print(2*int(s_diff))
        else:
            print(2*int(s_diff)+1)


explain = """
처음과 시작이 1이어야 한다는 조건 때문에 계단식으로 올랐다가 내려오는 구간이 반드시 존재해야 한다. 
이 구간에 대해서 총합은 n^2이므로 루트를 씌워 n을 구할 수 있다. 이때, n^2 + 2*n 까지 최대 2번을 반복해서 만들 수 있다. 
(만약 n^2+2*n +1 이 된다면 루트를 씌운 값이 n+1 이상이 된다) 또한 n이 계단의 최상이므로 n이하일 때는 1번을 더 해서 만들 수 있다.  
""" 