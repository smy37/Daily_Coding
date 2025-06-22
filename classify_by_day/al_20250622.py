import sys 

class TrieNode():
    def __init__(self):
        self.children = {}

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, chars):
        prefix = ""
        node = self.root
        flag = True
        for i, c in enumerate(chars):
            if flag:
                prefix += c
            if c not in node.children:
                node.children[c] = TrieNode()
                if flag:
                    flag = False
            node = node.children[c]
        return prefix
    
trie = Trie()
N = int(sys.stdin.readline())
memory = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    if word not in memory:
        memory[word] = 0
    memory[word] += 1
    pre = trie.insert(word)
    if memory[word] > 1:
        print(pre + f"{memory[word]}")
    else:
        print(pre)


explain = """
트라이의 기본 성질을 생각해 보면 다음과 같다. 단어를 넣었을 때, 해당 단어의 문자로 
경로를 만들고 만약 없느 경로라면 새로운 node가 추가된다. 따라서 기존에 이미 넣어준 
단어와 공통적인 부분, prefix로 되어 있는 node 까지는 새로운 node의 추가가 없지만
공통 prefix가 깨지는 부분부터 새로운 node가 추가된다. 그리고 여기까지 부분이 문제에서
핵심이 되는 별칭이 되는 부분이다.
"""