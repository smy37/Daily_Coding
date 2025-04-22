import sys

def gcd(a, b):
    temp_1 = min([a,b])
    temp_2 = max([a,b])
    while True:
        if temp_2 % temp_1 == 0:
            return temp_1
        temp_3 = temp_2
        temp_2 = temp_1
        temp_1 = temp_3 % temp_1

    return 1

ring_num = int(sys.stdin.readline())

ring_list = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, ring_num):
    temp = gcd(ring_list[0], ring_list[i])
    print(f'{ring_list[0]//temp}/{ring_list[i]//temp}')

