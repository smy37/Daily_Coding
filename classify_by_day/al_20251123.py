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
                        while s_idx <= e_idx:
                            if dp[s_idx][e_idx] == True:
                                dp[start][end] = True
                                if max_length < end-start:
                                    max_length = end-start
                                    ans = s[start:end+1]
                            s_idx +=1
                            e_idx -=1
        print(ans)
        return ans






if __name__ == "__main__":
    test_case = "cbbd"
    sol = Solution()
    sol.longestPalindrome(test_case)
