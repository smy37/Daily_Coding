from collections import deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer_str = ""
        t_memory = {}
        s_memory = {}
        idx_memory = {}

        for alpha in t:
            if alpha not in t_memory:
                t_memory[alpha] = 0
                s_memory[alpha] = 0
                idx_memory[alpha] = deque()
            t_memory[alpha] += 1

        answer = float("inf")
        left = 0
        for idx, alpha in enumerate(s):
            if alpha in t_memory:
                left = idx
                break

        for idx in range(left, len(s)):
            alpha = s[idx]
            if alpha in t_memory:
                if s_memory[alpha] < t_memory[alpha]:
                    s_memory[alpha] += 1
                    idx_memory[alpha].append(idx)
                elif s_memory[alpha] == t_memory[alpha]:
                    idx_memory[alpha].popleft()
                    idx_memory[alpha].append(idx)
                if s_memory == t_memory:
                    temp_min = float("inf")
                    for temp in idx_memory:
                        temp_min = min(temp_min, idx_memory[temp][0])
                    left = max(temp_min, left)
                    if answer > idx-left+1:
                        answer_str = s[left:idx + 1]
                        answer = idx-left+1
        return answer_str
