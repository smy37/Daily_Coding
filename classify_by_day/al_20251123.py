class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        max_length = -1
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for step in range(len(s)):
            for start in range(len(s)-step):
                end = start+step
                if step == 0:
                    dp[start][end] = True
                    if max_length < end - start:
                        max_length = end - start
                        ans = s[start:end + 1]
                elif step == 1 and s[start] == s[end]:
                    dp[start][end] = True
                    if max_length < end - start:
                        max_length = end - start
                        ans = s[start:end + 1]
                else:
                    if s[start] == s[end]:
                        s_idx = start+1
                        e_idx = end-1
                        if s_idx <= e_idx:
                            if dp[s_idx][e_idx] == True:
                                dp[start][end] = True
                                if max_length < end-start:
                                    max_length = end-start
                                    ans = s[start:end+1]

        return ans






if __name__ == "__main__":
    test_case = "abbcccba"
    sol = Solution()
    sol.longestPalindrome(test_case)
    explain = """
    Using the principle of dynamic programming, a bottom-up approach is the essential concept of this problem.
    If the start of the string is equal to the end of the string, 
    and the substring between them is a palindrome, 
    then this string is also a palindrome.
    """