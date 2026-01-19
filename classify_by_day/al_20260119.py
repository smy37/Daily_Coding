class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memory = {}
        for n in nums:
            if n not in memory:
                memory[n] = True
            else:
                del memory[n]

        for k in memory:
            return k
