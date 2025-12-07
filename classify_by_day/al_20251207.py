from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1_l = []
        num_2_l = []

        while l1.next:
            num_1_l.append(l1.val)
            l1 = l1.next
        num_1_l.append(l1.val)


        while l2.next:
            num_2_l.append(l2.val)
            l2 = l2.next
        num_2_l.append(l2.val)

        num_1 = 0
        for idx, val in enumerate(num_1_l):
            num_1 += val*(10**idx)

        num_2 = 0
        for idx, val in enumerate(num_2_l):
            num_2 += val * (10 ** idx)
        answer = []
        sum_n = str(num_1+num_2)
        for i in range(len(sum_n)):
            answer.append(sum_n[i])

        return answer


if __name__ == "__main__":
    explain = """
    To construct a linked list, we can use two approaches: recursion or a reverse-index method.
    """