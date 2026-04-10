import sys
from collections import deque

def checker(word1, word2):
    start = 0

    for i in range(len(word2)):
        if start == len(word1):
            break
        if word1[start] == word2[i]:
            start += 1

    if start == len(word1):
        return True
    else:
        return False
    
N, cri = sys.stdin.readline().split()
N = int(N)


answer = cri
word_graph = {}
for _ in range(N):
    cur_str = sys.stdin.readline().strip()
    if len(cur_str) not in word_graph:
        word_graph[len(cur_str)] = []
    word_graph[len(cur_str)].append(cur_str)

dq = deque()
dq.append(cri)
print(word_graph)
visit = {cri: True}
while dq:
    cur = dq.popleft()
    if len(answer) < len(cur):
        answer = cur
    
    if len(cur) + 1 in word_graph:
        word_list = word_graph[len(cur)+1]

        for word in word_list:
            print(word, word_graph)
            if checker(cur, word) and word not in visit:
                visit[word] = True
                dq.append(word)

print(answer)