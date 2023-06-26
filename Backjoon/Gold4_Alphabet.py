import copy
import sys

answer = 1
r, c = map(int, sys.stdin.readline().strip().split(' '))
board = []

visited = {}
for _ in range(r):
    temp = sys.stdin.readline().strip()
    board.append(temp)
    for i in temp:
        visited[ord(i)] = 0
max_num = len(visited)
def dfs(cr, visited, cur_len):
    global answer
    flag = False
    if cur_len == max_num:
        answer = max_num
        return
    for i in range(4):
        if i == 0 : # 동
            if cr[1]+1 < c and visited[ord(board[cr[0]][cr[1]+1])] == 0:
                flag = True
                t_copy = copy.deepcopy(visited)
                t_copy[ord(board[cr[0]][cr[1]+1])] = 1
                dfs([cr[0], cr[1]+1], t_copy, cur_len+1)
        elif i == 1:    # 서
            if cr[1] -1 >=0 and visited[ord(board[cr[0]][cr[1]-1])] == 0:
                flag = True
                t_copy = copy.deepcopy(visited)
                t_copy[ord(board[cr[0]][cr[1] - 1])] = 1
                dfs([cr[0], cr[1] - 1], t_copy, cur_len+1)
        elif i == 2:    # 남
            if cr[0] + 1 < r and visited[ord(board[cr[0]+1][cr[1]])] == 0:
                flag = True
                t_copy = copy.deepcopy(visited)
                t_copy[ord(board[cr[0]+1][cr[1]])] = 1
                dfs([cr[0]+1, cr[1]], t_copy, cur_len+1)
        elif i == 3:    # 북
            if cr[0] - 1 >= 0 and visited[ord(board[cr[0]-1][cr[1]])] == 0:
                flag = True
                t_copy = copy.deepcopy(visited)
                t_copy[ord(board[cr[0]-1][cr[1]])] = 1
                dfs([cr[0]-1, cr[1]], t_copy, cur_len+1)
    if flag == False:
        answer = max(answer, cur_len)

cur_str = board[0][0]
cur = [0,0]

visited[ord(cur_str)] = 1

dfs(cur, visited, 1)
print(answer)




