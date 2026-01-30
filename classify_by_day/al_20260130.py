class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1

        for i in range(n):
            if i + 1 <= n:
                dp[i+1] += dp[i]
            if i + 2 <= n:
                dp[i+2] += dp[i]

        return dp[-1]


if __name__ == "__main__":
    test_n = 5
    sol = Solution()
    print(sol.climbStairs(test_n))

explain = """
For each position, update the values of the reachable next positions.
"""
