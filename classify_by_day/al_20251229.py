from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = []
        cur_idx = 0
        temp = []
        while head:
            if cur_idx % 2== 0:
                temp = [head.val]
            elif cur_idx %2 == 1:
                temp = [head.val] + temp
                for v in temp:
                    if v != None:
                        answer.append(v)
                temp = []
            head = head.next
            cur_idx += 1
        if temp:
            for v in temp:
                answer.append(v)
        node = None
        for idx in range(len(answer)-1, -1, -1):
            node = ListNode(answer[idx], node)
        return node


if __name__ == "__main__":
    test_case = [0,4,9,2]
    test_node = None

    for idx in range(len(test_case)-1, -1, -1):
        test_node = ListNode(test_case[idx], test_node)

    sol = Solution()
    print(sol.swapPairs(test_node))

    explain = """
    First, extract and reorder the values into a list.  
    Second, construct a new linked list using this list.
    """