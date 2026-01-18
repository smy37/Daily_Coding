from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_map = {key:True for key in wordDict}
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] in hash_map:
                    dp[i][j] = 1

        def search(cur_idx, visit):
            if dp[cur_idx][-1]:
                return True
            for idx, end_string_idx in enumerate(dp[cur_idx]):
                if end_string_idx and idx+1 not in visit:

                    visit[idx+1] = True
                    flag = search(idx+1, visit)
                    if flag: return True
            return False

        answer = search(0, {})
        
        return answer



if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    sol.wordBreak(s, wordDict)