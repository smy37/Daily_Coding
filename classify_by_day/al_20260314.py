from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ## First Approach
        memory = {}
        cur = 0
        for idx in range(len(nums)):
            num = nums[idx]
            if num in memory:
                return True
            memory[num] = 1
            if idx - cur + 1 > k:
                memory[nums[cur]] -= 1
                if memory[nums[cur]] == 0:
                    del memory[nums[cur]]
                cur += 1

        return False

        ## Second Approach
        memory = {}

        for idx, num in enumerate(nums):
            if num in memory and abs(idx - memory[num]) <=k:
                return True
            memory[num] = idx
        return False

explain = """The key idea of the sliding window technique is to update the window position or size 
when past positions no longer need to be considered.
"""