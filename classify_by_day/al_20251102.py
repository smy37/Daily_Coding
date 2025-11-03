import sys
from itertools import combinations

num_l = [10]

for i in range(2, 11):
    temp = 1
    for j in range(i):
        temp *= ((10-j)/(j+1))
    num_l.append(int(temp))
N = int(sys.stdin.readline())

acc = 0
for i in range(len(num_l)):
    acc += num_l[i]

    if acc > N:
        acc -= num_l[i]
        rest = N-acc
        cri = i + 1
        num = sorted(list(combinations(range(9, -1, -1), cri)))[rest]
        print(int("".join(map(str, num))))
        break
else:
    print(-1)

explain = """
내림수라는 것을 조합과 같다는 것을 이용해 자리수를 구한다. 자리수가 정해진다면 COMBINATION
을 통해서 N번째 수를 확정한다.
"""