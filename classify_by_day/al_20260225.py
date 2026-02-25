# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []
        memory = {}
        while head:

            if head.val not in memory:
                node_list.append(head)
                memory[head.val] = True
            head = head.next

        cur = None
        for i in range(len(node_list) - 1, -1, -1):
            node_list[i].next = cur
            cur = node_list[i]
        return cur


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_list = []
        even_list = []

        cnt = 0

        while head:
            if cnt % 2 == 0:
                odd_list.append(ListNode(head.val, None))
            else:
                even_list.append(ListNode(head.val, None))
            head = head.next
            cnt += 1
        cur = None
        for i in range(len(even_list) - 1, -1, -1):
            even_list[i].next = cur
            cur = even_list[i]
        for i in range(len(odd_list) - 1, -1, -1):
            odd_list[i].next = cur
            cur = odd_list[i]
        return cur