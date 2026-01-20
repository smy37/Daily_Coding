from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = len(nums) - 2

        for i in range(idx, -1, -1):
            idx = i
            if nums[i] < nums[i + 1]:
                break

        min_v = nums[idx + 1]
        min_idx = len(nums) - 1
        for i in range(idx + 1, len(nums)):
            if nums[i] > nums[idx]:
                min_idx = i
                if min_v > nums[i]:
                    min_v = nums[i]
                    min_idx = i

        temp = nums[min_idx]
        nums[min_idx] = nums[idx]
        nums[idx] = temp
        nums[idx + 1:] = sorted(nums[idx + 1:])

