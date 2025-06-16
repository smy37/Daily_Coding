import sys 
import math

answer = 0
N = int(sys.stdin.readline())

if math.sqrt(N)%1 == 0:
    print(-1)
    sys.exit()
else:
    for i in range(1, int(math.sqrt(N))+1):
        j = N/i
        if j%1 == 0:
            b = (j+i)/2
            a = (j-i)/2
            if a%1 == 0 and b%1 == 0 and a>0 and b>0:
                answer += 1
        
        b = math.sqrt(N-i**2)
        if b >= i and b%1 == 0:
            answer += 1
print(answer)

explain = """
N이 주어졌을 때, a^2+b^2 = N 과 a^2+N = b^2인 경우를 나눠서 카운팅 해준다. 
a^2+N = b^2 인 경우에 N = (b-a)(b+a)로 바꿔서 생각하고 b-a와 b+a가 모두 정수이고 b, a 모두 정수가 되는 개수를 카운팅 해준다.
"""