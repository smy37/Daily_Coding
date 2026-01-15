from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def search(cur_node):
            val = cur_node.val
            if cur_node.left and cur_node.right:
                left_val, left_max, flag_left = search(cur_node.left)
                right_min, right_val, flag_right = search(cur_node.right)
                flag = False
                if left_max < val < right_min and (flag_left and flag_right):
                    flag = True
                return left_val, right_val, flag
            elif cur_node.left:
                left_val, left_max, flag = search(cur_node.left)
                if left_max >= val:
                    flag = False
                return left_val, val, flag
            elif cur_node.right:
                right_min, right_val, flag = search(cur_node.right)
                if val >= right_min:
                    flag = False
                return val, right_val, flag
            else:
                return val, val, True
        _, _, answer = search(root)
        return answer

explain = """
Use DFS to traverse down to the leaf nodes.  
Update the maximum value in the left subtree and the minimum value in the right subtree.  
"""