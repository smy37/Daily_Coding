import sys
import math
from math import gcd

div, mul = map(int, sys.stdin.readline().split())

cri = mul//div

for i in range(int(math.sqrt(cri)), 0, -1):
    if cri %i == 0:
        j = cri // i
        if gcd(i, j) == 1:
            print(i*div, j*div)
            sys.exit()


explain = """
최소공배수를 최대공약수로 나눈 수를 소인수분해 했을 때, 소인수분해 한 것을 수 2개로 분배했을 때, 
이 2개의 수는 서로 약수가 생기면 안된다. 왜냐하면 이미 최대공약수를 구했고 약수가 생기면 최대공약수에 이 약수를 
곱한 수가 공약수가 되는 것이므로 모순이 생긴다. 따라서 분배된 2개의 수가 서로 약수가 생기지 않고(gcd = 1) 중앙에 있는
수부터 이 수를 찾아 가는 로직으로 풀이 가능하다.
"""