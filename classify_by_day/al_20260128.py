class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_memory, min_memory = -float("inf"), float("inf")
        dp = [1, 1]
        for n in nums:
            first, second = n*dp[0], n*dp[1]
            temp_max = max(first, second, n)
            temp_min = min(first, second, n)

            dp[0] = temp_max
            dp[1] = temp_min

            max_memory = max(max_memory, temp_max)
            min_memory = min(min_memory, temp_min)

        return max_memory
