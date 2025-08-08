import sys
import math
from itertools import permutations
def check_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i ==0:
            return False
    return True

c = int(sys.stdin.readline())

for _ in range(c):
    answer = 0
    cur_n = sys.stdin.readline().strip()
    memory = {}
    for i in range(1, len(cur_n)+1):
        for comb in permutations(range(len(cur_n)), i):
            num = int("".join([cur_n[i] for i in comb]))
            if num not in memory:
                if check_prime(num):
                    answer += 1
                memory[num] = 1
    print(answer)

explain = """
소수를 판별하는 함수를 제곱근을 이용하여 구현후에 1개부터 길이만큼의 순열을
통해 만들 수 있는 수가 소수인지 판단한다.
"""