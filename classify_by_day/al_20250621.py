import sys
from collections import deque

## 1. First Try (Using Trie)
# answer = 0
#
# class TrieNode():
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#
# class Trie():
#     def __init__(self):
#         self.root = TrieNode()
#
#     def insert(self, chars):
#         global answer
#         node = self.root
#         for c in chars:
#             if c not in node.children:
#                 node.children[c] = TrieNode()
#                 answer += 1
#             node = node.children[c]
#         node.is_end = True
#
# N, K = map(int, sys.stdin.readline().split())
# trie_front = Trie()
# trie_back = Trie()
# inserted_front = set()
# inserted_back = set()
#
# for _ in range(N):
#     t_str = sys.stdin.readline().strip()
#     front = t_str[:K]
#     back = t_str[-1:-(K+1):-1]
#
#     if front not in inserted_front:
#         trie_front.insert(front)
#         inserted_front.add(front)
#
#     if back not in inserted_back:
#         trie_back.insert(back)
#         inserted_back.add(back)
#
# print(answer)


### 2. Second Try
def cnt_prefix(a, b):
    i = 0
    while i < K and a[i] == b[i]:
        i += 1
    return i

N, K = map(int, sys.stdin.readline().split())
front, back = [], []

for _ in range(N):
    s = sys.stdin.readline().strip()
    front.append(s[:K])
    back.append(s[-1:-(K+1):-1])

front.sort()
back.sort()

answer = 0
for i in range(1, N):
    answer += cnt_prefix(front[i-1], front[i])
    answer += cnt_prefix(back[i-1], back[i])

print(2*N*K - answer)


explain = """
첫번째 시도에서 트라이를 2개 만들어서 앞에서 K번째 까지 트라이에 넣어주고 뒤에서 K번까지 트라이에 넣어줘서 
정점의 개수를 셌다. 그러나 이는 메모리 초과를 발생시켜서 다른 접근이 필요하였다. 
트라이에 정점이 추가되는 과정을 생각해보면 prefix(접두사)가 같은 부분까지는 새로운 node가 생기지 않고 기존의 
node를 사용한다. 따라서 전체 문자의 개수가 2*N*K이고 N개의 문자열을 정렬 후에 양 옆에 것들을 비교해서 prefix의 길이를 모두 합친 값을 
answer 라고 한다면 최종 소요되는 node의 개수는 2*N*K-answer가 된다. prefix는 공유하므로...
"""