# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global answer
        answer = root.val
        num_list = []
        leaf_node = []

        def dfs(root):
            global answer

            left_val, right_val = 0, 0
            if root.left:
                left_val = dfs(root.left)
            if root.right:
                right_val = dfs(root.right)
            left_val = max(left_val, 0)
            right_val = max(right_val, 0)
            val = max(left_val + root.val, right_val + root.val)
            answer = max(answer, left_val + right_val + root.val, val)
            return val

        cur = dfs(root)
        answer = max(cur, answer)
        return answer
