import sys 

class TrieNode():
    def __init__(self):
        self.childs = {}
        self.is_end = False

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, chars):
        node = self.root
        for c in chars:
            if c not in node.childs:
                node.childs[c] = TrieNode()
            node = node.childs[c]
        node.is_end = True

    def search(self, chars):
        node = self.root
        for c in chars:
            if c not in node.childs:
                return False
            node = node.childs[c]
        return True

seq = ["A", "T", "G", "C"]

def get_candidate(cur, end):
    answer = []
    if len(cur) == end:
        return [cur]
    for s in seq:
        answer += get_candidate(cur+s, end)
    return answer

dna = sys.stdin.readline().strip()

for n in range(1, 7):
    candi = get_candidate("", n)
    trie = Trie()
    for i in range(len(dna)-n+1):
        trie.insert(dna[i:i+n])
    for c in candi:
        if not trie.search(c):
            print(c)
            sys.exit()


explain = """
트라이에 대한 질문을 받았었어서 트라이를 이용하는 문제를 풀었다. 
python 기본 자료형이 아닌 자료구조를 새롭게 만들어서 푸는 문제는 생소하지만
몇번 구현해보니 트라이의 개념을 어렵지 않게 이해할 수 있었다. 
위 문제에서는 처음에 for n in range(1, 6)을 했고 그 이유는 
염기서열 5개가 붙은 것이 총 4^5 = 1024개 이므로 최소 1024*5 = 5120 길이의 문자열이
필요하다고 생각하였는데 사실상 최단 길이는 4^n + n -1이라고 한다. 
de Brujin sequence에 의해 해당 최소길이가 나온다고 하는데 추후에 학습이 필요하다.
"""