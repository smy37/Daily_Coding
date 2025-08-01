import sys
import math

G = int(sys.stdin.readline())
avaliable_weight = []
for i in range(math.ceil(math.sqrt(G)), G+1):
    if G % i == 0:
        j = G // i
        if (i+j)%2 == 0 and (i-j)%2 == 0 and i > j:
            avaliable_weight.append((i+j)//2)

if len(avaliable_weight) == 0:
    print(-1)
else:
    for i in avaliable_weight:
        print(i)

explain = """
G = (A+B)(A-B) 로 바꾼 후 정수가 되는 A와 B를 구한다. 또한 A>B 조건을 만족해야 한다.
그리고 A값을 찾을 때, math.ceil(math.sqrt(G)) 부터 G까지 수가 후보가 된다.
"""