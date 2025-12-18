class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf") for _ in range(n+1)]
        dp[0] = 0
        square_num_list = [i**2 for i in range(1, int(n**0.5)+1)]

        for i in range(len(dp)):
            for num in square_num_list:
                if i+num <= n:
                    dp[i+num] = min(dp[i+num], dp[i]+1)
        return dp[-1]

if __name__ == "__main__":
    t_n = 13
    sol = Solution()
    print(sol.numSquares(t_n))

    explain = """
    We can consider the num_square list first rather than the memory index.
    It is also possible to consider the memory index first rather than the num_square list.
    """
