from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        ## 1. First Appraoch
        # hash_map = {key:True for key in wordDict}
        # dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j+1] in hash_map:
        #             dp[i][j] = 1
        #
        # def search(cur_idx, visit):
        #     if dp[cur_idx][-1]:
        #         return True
        #     for idx, end_string_idx in enumerate(dp[cur_idx]):
        #         if end_string_idx and idx+1 not in visit:
        #
        #             visit[idx+1] = True
        #             flag = search(idx+1, visit)
        #             if flag: return True
        #     return False
        #
        # answer = search(0, {})

        ## 2. Second Approach.
        n = len(s)
        word_hash = {word: True for word in wordDict}
        length_list = [len(word) for word in wordDict]
        min_length, max_length = min(length_list), max(length_list)
        dp = [False for _ in range(n+1)]
        dp[0] = True

        for i in range(1, n+1):
            start = max(0, i-max_length)
            end = i-min_length

            for j in range(start, end+1):
                if dp[j] and s[j:i] in word_hash:
                    dp[i] = True
        return dp[n]



if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    sol.wordBreak(s, wordDict)