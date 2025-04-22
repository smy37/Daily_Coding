import sys
from collections import deque

dq = deque()
n, m = map(int, sys.stdin.readline().strip().split(' '))
enter_dic = {}
outer_dic = {}
for i in range(n):
    enter_dic[i+1] = 0
    outer_dic[i+1] = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().strip().split(' ')))
    enter_dic[temp[1]] +=1
    outer_dic[temp[0]].append(temp[1])

visited = {}
for i in enter_dic:
    if enter_dic[i] == 0:
        dq.append(i)
        visited[i] = 0
result = []
del_list = []

while dq:
    t_n = dq.popleft()
    print(t_n, end= ' ')
    for i in outer_dic[t_n]:
        if i in enter_dic:
            enter_dic[i] -=1
            if enter_dic[i] == 0:
                dq.append(i)
    ### 주의사항 !!!
    ### 처음에는 아래와 같은 방법을 통해 시간초과가 발생하였다... 그러나 생각해보면 enter_dic[i]가 0이 되는 순간 outer_dic에서 i원소가 발생할 수 없다.....
    # for i in enter_dic:
    #     if enter_dic[i] == 0 and i not in visited:
    #         dq.append(i)
    #         visited[i] = 0

