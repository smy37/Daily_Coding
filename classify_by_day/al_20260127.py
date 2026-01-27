# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        global node_num
        global answer
        answer = {}
        node_num = 0

        def search(cur_node, acc_list):
            global node_num
            global answer
            node_num += 1
            acc_list = acc_list + [[node_num, acc_list[-1][1] + cur_node.val]]
            if not cur_node.left and not cur_node.right:
                for i in range(len(acc_list)):
                    for j in range(i + 1, len(acc_list)):
                        if acc_list[j][1] - acc_list[i][1] == targetSum:

                            if (acc_list[j][0], acc_list[i][0]) not in answer:
                                answer[(acc_list[j][0], acc_list[i][0])] = True

            else:
                if cur_node.left:
                    search(cur_node.left, acc_list)
                if cur_node.right:
                    search(cur_node.right, acc_list)

        if root:
            search(root, [[0, 0]])
        return len(answer.keys())