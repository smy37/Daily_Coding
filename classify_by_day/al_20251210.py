from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0,0] for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            dp[i][0] = max(dp[i-1])
            dp[i][1] = dp[i-1][0] + nums[i-1]
        return max(dp[-1])


if __name__ == "__main__":
    test_case = [1,2,3,1]
    sol = Solution()
    print(sol.rob(test_case))

    explain = """
    When reaching two consecutive targets is impossible, we only need to consider the current position and the previous one.  
    There is no need to think about positions two steps away.
    """