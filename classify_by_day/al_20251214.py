class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        answer = dp[-1][-1]

        return answer


if __name__ == "__main__":
    t1, t2 = "abcdestg", "saceg"
    sol = Solution()
    print(sol.longestCommonSubsequence(t1, t2))

    explain = """
    The core idea of solving the LCS problem with dynamic programming is to define dp[i][j] 
    as the length of the longest common subsequence between text1[0..i] and text2[0..j].
    If text1[i] == text2[j], then:
    dp[i][j] = dp[i-1][j-1] + 1.
    Otherwise, dp[i][j] is obtained by taking the maximum of:
    - dp[i-1][j] (excluding text1[i])
    - dp[i][j-1] (excluding text2[j]).
    """
