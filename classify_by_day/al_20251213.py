class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float("inf") for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)+1):
            dp[i][0] = i
        for i in range(len(word2)+1):
            dp[0][i] = i

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1]+1, dp[i+1][j]+1, dp[i][j]+1)
        return dp[-1][-1]

if __name__ == "__main__":
    word1, word2 = "intention", "execution"
    sol = Solution()
    print(sol.minDistance(word1, word2))

    explain = """
    Main logic of this problem is similar with LCS(Longest Common Subsequence). 
    """