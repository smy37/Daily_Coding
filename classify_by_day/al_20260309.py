# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        memory = set()
        while head:
            if head in memory:
                return True
            else:
                memory.add(head)
                head = head.next

        return False

        ## Two pointer approach
        # idx1, idx2 = head, head
        #
        # while idx2 and idx2.next:
        #     idx1 = idx1.next
        #     idx2 = idx2.next.next
        #
        #     if idx1 == idx2:
        #         return True
        # return False