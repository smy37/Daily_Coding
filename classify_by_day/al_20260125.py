# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import heapq
from typing import Optional

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## 1. First Approach
        # hq = []
        #
        # def search(cur_node):
        #     heapq.heappush(hq, cur_node.val)
        #
        #     if cur_node.left:
        #         search(cur_node.left)
        #     if cur_node.right:
        #         search(cur_node.right)
        #
        # if root:
        #     search(root)
        #
        # cur = None
        # for _ in range(k):
        #     cur = heapq.heappop(hq)
        # return cur

        ## 2. Second Approach
        cur_index = 0
        answer = None
        def search(cur_node):
            global cur_index
            global answer
            if cur_node.left:
                search(cur_node.left)

            cur_index += 1
            if cur_index == k:
                answer = cur_node.val

            if cur_node.right:
                search(cur_node.right)

        return answer

explain = """
In a BST, all elements in the left subtree are smaller than the root value, 
and all elements in the right subtree are larger than the root value. 
"""