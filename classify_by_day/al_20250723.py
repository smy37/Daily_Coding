import sys

R, C = map(int, sys.stdin.readline().split())
str_list = ["" for _ in range(C)]
for _ in range(R):
    cur_str = sys.stdin.readline().strip()
    for i in range(C):
        str_list[i] += cur_str[i]

answer = 0

for s in range(1, R):
    memory = set()
    for i in range(C):
        memory.add(str_list[i][s:])

    if len(memory) != C:
        break
    answer += 1

print(answer)

explain = """
새로로 읽은 문자열을 저장해두고 단계가 진행될때마다 시작 인덱스를 갱신하여 해당 인덱스부터
시작하는 문자열을 set 자료구조에 넣어준다. set의 크기가 column의 크기와 다르다면 겹치는 
문자열이 발생하는 경우이고 이때, 종료한다.
"""