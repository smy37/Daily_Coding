from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        val_list = []

        while head.next:
            val_list.append(head.val)
            head = head.next
        val_list.append(head.val)
        del val_list[len(val_list) - n]
        cur_node = None

        for i in range(len(val_list) - 1, -1, -1):
            pre_node = ListNode(val_list[i], cur_node)
            cur_node = pre_node
        head = cur_node

        return head

    ## another approach
    # def dfs(self, cur_node, target_n):
    #     if cur_node.next == None:
    #         return 1, cur_node
    #     cnt, next_node = self.dfs(cur_node.next, target_n)
    #     if cnt == target_n:
    #         cur_node.next = next_node.next
    #     return cnt+1, cur_node
    #
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     if not head.next:
    #         return None
    #     idx, result = self.dfs(head, n)
    #     if idx == n:
    #         return result.next
    #     else:
    #         return result

explain = """
I solved this problem in two ways. 
The first approach extracts the values, modifies them, and then builds a new linked list. 
The second approach uses recursion to exclude the target node.
"""