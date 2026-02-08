class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        memory = {n + 1: 0 for n in range(len(nums))}

        for n in nums:
            memory[n] += 1

        left, right = -1, -1
        for n in memory:
            if memory[n] == 0:
                right = n
            elif memory[n] == 2:
                left = n

        return [left, right]
