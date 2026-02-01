from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_memory = {}

        def search(cur_node):
            if cur_node in node_memory:
                return cur_node
            node_memory[cur_node] = True
            if cur_node.next:
                return search(cur_node.next)

        if head:
            return search(head)
