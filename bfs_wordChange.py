from collections import deque

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]


def compare(word1:str, word2:str):
    temp = 0
    result = True
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            temp+=1
        if temp >1:
            result = False
            break
    return result



def solution(begin, target, words):

    words.append(begin)
    answer = 0
    graph = {}
    length = {}
    for i in words:
        graph[i] = []
        length[i] = 0
    if target not in graph:
        return 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            temp = compare(words[i], words[j])
            if temp:
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    stack = []
    visited = []
    stack = deque(stack)
    stack.append(begin)
    while stack:
        t_word = stack.popleft()
        if t_word not in visited:
            visited.append(t_word)
            for i in graph[t_word]:
                if i not in visited:
                    stack.append(i)
                    length[i] = length[t_word] +1
                if i==target:
                    answer = length[target]
                    return answer
    answer = length[target]
    return answer

print(solution(begin, target, words))