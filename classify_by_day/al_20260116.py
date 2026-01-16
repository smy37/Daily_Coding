from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        memory = {}

        def search(node, level):
            if level not in memory:
                memory[level] = []
            memory[level].append(node.val)
            if node.left:
                search(node.left, level + 1)
            if node.right:
                search(node.right, level + 1)

        answer = []
        if root:
            search(root, 0)
            level = max(memory.keys())
            for i in range(level + 1):
                answer.append(memory[i])
        return answer

explain = """
Use DFS to traverse the nested structure while maintaining a stack to store the traversal state.
"""