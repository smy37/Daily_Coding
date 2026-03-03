# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_list = []

        while head:
            node_list.append(ListNode(head.val))
            head = head.next

        for i in range(len(node_list)):
            for j in range(i - 1, -1, -1):
                if node_list[j + 1].val < node_list[j].val:
                    temp = node_list[j].val
                    node_list[j].val = node_list[j + 1].val
                    node_list[j + 1].val = temp
                else:
                    break

        next = None
        for i in range(len(node_list) - 1, -1, -1):
            node_list[i].next = next
            next = node_list[i]

        return next

    ## Fast Method
    # def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     node_list = []
    #
    #     while head:
    #         node_list.append(head.val)
    #         head = head.next
    #
    #     node_list.sort()
    #
    #     next = None
    #
    #     for i in range(len(node_list) - 1, -1, -1):
    #         cur = ListNode(node_list[i], next)
    #         next = cur
    #
    #     return next
