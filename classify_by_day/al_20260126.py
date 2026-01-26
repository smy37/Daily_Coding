# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        num_list = []

        def search(cur_node):
            num_list.append(cur_node)
            if cur_node.left:
                search(cur_node.left)

            if cur_node.right:
                search(cur_node.right)

        if root:
            search(root)

        if num_list:
            for i in range(len(num_list) - 1):
                num_list[i].left = None
                num_list[i].right = num_list[i + 1]


explain = """
Assigning a new value inside a function does not change the value outside its scope.
"""