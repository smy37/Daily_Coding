from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(temp_pre, temp_in):
            if not temp_pre:
                return None

            root = temp_pre[0]
            if len(temp_pre) == 1:
                return TreeNode(root)
            i = temp_pre.index(root)

            left_temp = temp_in[:i]
            right_temp = temp_in[i + 1:]

            left_set = set(left_temp)
            right_set = set(right_temp)

            left_pre = []
            right_pre = []

            for n in temp_pre:
                if n in left_set:
                    left_pre.append(n)
                elif n in right_set:
                    right_pre.append(n)

            left_tree = build(left_pre, left_temp)
            right_tree = build(right_pre, right_temp)

            return TreeNode(root, left_tree, right_tree)

        tree = None
        if preorder:
            tree = build(preorder, inorder)

        return tree

sol = Solution()
print(sol.buildTree([3,9,20,15,7], [9,3,15,20,7]))

explain = """
In inorder traversal, elements on the left of the root belong to the left subtree, 
and elements on the right belong to the right subtree.  
In preorder traversal, the first element is always the root, 
so we can identify the root recursively. 
"""