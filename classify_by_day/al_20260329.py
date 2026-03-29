# class TrieNode():
#     def __init__(self, name):
#         self.children = {}
#         self.is_end = False
#         self.name = name

class Trie:
    # def __init__(self):
    #     self.root = TrieNode("root")
    #
    # def insert(self, word: str) -> None:
    #     node = self.root
    #     for c in word:
    #         if c not in node.children:
    #             node.children[c] = TrieNode(c)
    #         node = node.children[c]
    #     node.is_end = True
    #
    # def search(self, word: str) -> bool:
    #     node = self.root
    #     for c in word:
    #         if c not in node.children:
    #             return False
    #         node = node.children[c]
    #     if node.is_end == True:
    #         return True
    #     else:
    #         return False
    #
    # def startsWith(self, prefix: str) -> bool:
    #     node = self.root
    #     for c in prefix:
    #         if c not in node.children:
    #             return False
    #         node = node.children[c]
    #     return True

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["is_end"] = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        if "is_end" in node:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)