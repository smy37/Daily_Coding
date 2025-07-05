import sys 

N = int(sys.stdin.readline())
num_l = list(map(int, sys.stdin.readline().split()))
s = []
answer = [0 for _ in range(N)]
for i in range(N-1, -1, -1):
    if len(s) == 0:
        s.append([num_l[i], i])
    else:
        while len(s) > 0 and s[-1][0] < num_l[i]:
            answer[s[-1][1]] = i+1
            s.pop()
        s.append([num_l[i], i])

for i in answer:
    print(i, end=" ")


explain = """
끝에서 부터 왼쪽으로 가면서 현재 위치의 높이가 stack에 있는 값보다 크다면 stack에 있는 값들은
현재 높이의 빌딩과 만나는 것.
"""