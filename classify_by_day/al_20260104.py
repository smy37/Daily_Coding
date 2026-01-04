from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## First Approach
        # for l in range(len(s), 1, -1):
        #     idx = 0
        #     while idx <= len(s) - l:
        #         temp_dict = {}
        #
        #         for i in range(idx, idx+l):
        #             c = s[i]
        #             if c not in temp_dict:
        #                 temp_dict[c] = True
        #                 if len(temp_dict) == l:
        #                     return l
        #             else:
        #                 idx += 1
        #                 break
        #
        # if len(s) == 0:
        #     return 0
        # else:
        #     return 1

        ## Second Approach
        answer = 0
        char_dict = {}
        start = 0
        for end, c in enumerate(s):
            if c in char_dict:
                start = max(start, char_dict[c]+1)
            char_dict[c] = end
            answer = max(answer, end-start+1)

        return answer
if __name__ == "__main__":
    test_case = "dvdf"
    sol = Solution()
    print(sol.lengthOfLongestSubstring(test_case))

    explain = """
    Update the start of the window using a character dictionary that records the last index of each character.
    """