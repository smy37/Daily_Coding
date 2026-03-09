from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        ## 1. Brute Force Approach
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > 2*nums[j]:
                    answer += 1

        return answer

        ## 2. Merge Sort Approach