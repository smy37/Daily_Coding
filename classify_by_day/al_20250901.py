import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
min_cri = 0
for n in num_list:
    if n >0:
        min_cri = n

for i in range(min_cri, 0, -1):
    cri = num_list[0]%i
    for j in range(1, len(num_list)):
        if cri != num_list[j]%i:
            break
    else:
        print(i)
        break

explain ="""
위 로직이 시간초과가 발생할거라고 생각했는데 시간초과 없이 통과하였다.
더 빠른 로직을 생각했는데 가장 작은 양수를 cri라고 하면 cri 보다 작은 양의 정수를
전체에 빼주고 전체의 최대 공약수를 구하면 된다.
"""