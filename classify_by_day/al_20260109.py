from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = []
        for n in nums:
            if len(memory) == 0:
                memory.append(n)
                continue
            idx = bisect_left(memory, n)

            if memory[-1] < n:
                memory.append(n)
            else:
                memory[idx] = n
        return len(memory)


explain = """
Find the optimal position for the current number using binary search.
"""