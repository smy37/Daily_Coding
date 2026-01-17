from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        memory = {}

        def search(node, level):
            if level not in memory:
                memory[level] = []

            memory[level].append(node.val)

            if node.left:
                search(node.left, level+1)
            if node.right:
                search(node.right, level+1)

        print(memory)

explain = """
Traverse the binary tree using DFS, then find the rightmost node at each level.
"""