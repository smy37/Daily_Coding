import sys
from itertools import permutations

N = int(sys.stdin.readline())
flag = False
if N > 184010 or N < 38210:
    print("No Answer")
    sys.exit()
for iter in permutations(range(10), 7):
    h, w, e, o, l, r, d = iter
    if h==0 or w == 0:
        continue

    if (o+d)%10 != N%10:
        continue
    num1 = (h)*10000 + (e)*1000 + (l)*100 + (l)*10 + o
    num2 = (w)*10000 + (o)*1000 + (r)*100 + (l)*10 + d
    cri = num1+num2

    if cri == N:
        print(" ", num1)
        print("+", num2)
        print("-------")
        print(" "*(6-len(str(cri))), cri)
        flag = True
        break

if not flag:
    print("No Answer")

explain = """
0부터 9까지의 수를 10p7 의 경우의 수를 구한 다음에 조건을 만족하는지 체크해준다. 
마지막 수의경우 공백이 합에 따라 달라지므로 그부분을 유의한다.
"""

