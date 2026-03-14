class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        ## 1. First Approach
        # answer = 0
        # memory = {}
        # for idx, v in enumerate(s):
        #     if v not in memory:
        #         memory[v] = []
        #     memory[v].append(idx)
        #     if len(memory[v]) + k >= idx + 1:
        #         answer = max(answer, min(len(memory[v]) + k, len(s)))
        #
        #     else:
        #         for i_idx, i in enumerate(memory[v]):
        #             if (idx - i - 1) - (len(memory[v]) - i_idx - 2) <= k:
        #                 answer = max(answer, idx - i + 1)
        #
        #                 break
        #
        # return answer

        ## 2. Second Approach
        answer = 0
        left = 0

        memory = {}

        for right, char in enumerate(s):
            if char not in memory:
                memory[char] = 0
            memory[char] += 1
            max_cnt = max(memory.values())

            while (right-left+1)-max_cnt > k:
                memory[s[left]] -=1
                left += 1

            answer = max(answer, right-left+1)

        return answer

explain = """The maximum possible valid length is (max_frequency + k) within the current window of length (right - left + 1).
If (right - left + 1) becomes greater than (max_frequency + k), 
we move the left pointer forward by one. 
This is because it is impossible to form a valid window of length (right - left + 1) with at most k replacements.
"""