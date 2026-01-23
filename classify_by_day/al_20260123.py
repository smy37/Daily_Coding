from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_list = []
        def search(cur_node):
            num_list.append(cur_node.val)
            if cur_node.next:
                search(cur_node.next)
        if head:
            search(head)
        num_list.sort()

        current = None
        for i in range(len(num_list) - 1, -1, -1):
            current = ListNode(num_list[i], current)

        return current