# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        anc_p = []
        anc_q = []

        def search(cur_node, acc_anc):
            if cur_node == p:
                anc_p[:] = acc_anc + [cur_node]
            elif cur_node == q:
                anc_q[:] = acc_anc + [cur_node]

            if cur_node.left:
                search(cur_node.left, acc_anc + [cur_node])
            if cur_node.right:
                search(cur_node.right, acc_anc + [cur_node])

        search(root, [])
        answer = None

        if len(anc_p) >= len(anc_q):
            temp = {}
            for i in range(len(anc_q) - 1, -1, -1):
                temp[anc_q[i].val] = True
            for i in range(len(anc_p) - 1, -1, -1):
                val = anc_p[i].val
                if val in temp:
                    answer = anc_p[i]
                    break
        else:
            temp = {}
            for i in range(len(anc_p) - 1, -1, -1):
                temp[anc_p[i].val] = True
            for i in range(len(anc_q) - 1, -1, -1):
                val = anc_q[i].val
                if val in temp:
                    answer = anc_q[i]
                    break
        return answer