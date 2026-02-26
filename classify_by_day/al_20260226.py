## Problem 1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []

        while head:
            node_list.append(ListNode(head.val))
            head = head.next

        cur = None
        for i in range(len(node_list)):
            node_list[i].next = cur
            cur = node_list[i]

        return cur

## Problem 2.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}

        for idx, n in enumerate(nums):
            if target-n in memory:
                return [idx, memory[target-n]]
            memory[n] = idx

