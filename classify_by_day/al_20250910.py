import sys

a, d = map(int, sys.stdin.readline().split())

def get_num(k):
    return a+(k-1)*d

def gcd(a, b):
    r = a % b
    if r== 0:
        return b
    return gcd(b, r)

q_num = int(sys.stdin.readline())

for _ in range(q_num):
    q, l, r = map(int, sys.stdin.readline().split())

    if q == 1:
        print((r-l+1)*(get_num(l)+get_num(r))//2)
    elif q == 2:
        if l == r:
            print(get_num(l))
        else:
            if d == 0:
                print(a)
            else:
                a1 = get_num(l)
                print(gcd(a1, d))

explain="""
나머지 연산의 성질이 매우 중요하게 작용한다. 최대공약수를 구할 때, 나누는 수와 나머지의 최대공약수가 원래의
최대공약수가 되는 성질이 있다. 또한 유사하게 모든 등차수열은 초항과 공차는 공통으로 가지고 있으므로 등차수열의
최대공약수는 초항과 공차의 최대공약수를 구하는 것으로 된다.
"""