from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        dq = deque([[idx, value] for idx, value in enumerate(tickets)])
        cur = 0
        while dq:
            cur += 1
            idx, rest_value = dq.popleft()
            if rest_value-1 == 0:
                if idx == k:
                       return cur
            else:
                dq.append([idx, rest_value-1])
        return cur
