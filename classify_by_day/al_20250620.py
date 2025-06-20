import sys

class TrieNode():
    def __init__(self, name):
        self.children = {}
        self.is_end = False
        self.cur_name = name

class Trie():
    def __init__(self):
        self.root = TrieNode("root")

    def insert(self, chars):
        node = self.root

        for c in chars:
            if c not in node.children:
                node.children[c] = TrieNode(c)
            node = node.children[c]
        node.is_end = True

answer = []

def get_order(cur_node: TrieNode, depth, b_root):
    if not b_root:
        answer.append(" " * depth + cur_node.cur_name)
    order = sorted(cur_node.children.keys())
    for child in order:
        get_order(cur_node.children[child], depth + 1, False)


trie = Trie()

N = int(sys.stdin.readline())

for _ in range(N):
    t_str = [t.strip() for t in sys.stdin.readline().split("\\")]
    trie.insert(t_str)
get_order(trie.root, -1, True)

for i in answer:
    print(i)


explain = """
파일 경로를 백슬래시(\)로 split 후에 트라이에 넣어준다. 
그후에 사전 순서대로 트라이의 노드를 조회해주는데 이때, 재귀를 이용하여 조회해준다.
"""