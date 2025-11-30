from typing import List
from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter = {2:["a", "b", "c"],
                           3:["d", "e", "f"],
                           4: ["g", "h", "i"],
                           5: ["j", "k", "l"],
                           6: ["m", "n", "o"],
                           7: ["p", "q", "r", "s"],
                           8: ["t", "u", "v"],
                           9: ["w", "x", "y", "z"],
                           }
        dq = deque()
        dq.append("")
        for num in digits:
            new_dq = deque()
            while dq:
                cur = dq.popleft()
                for s in digit_to_letter[int(num)]:
                    new_dq.append(cur+s)
            dq = new_dq

        return list(dq)

if __name__ == "__main__":
    test_case = "23"
    solution = Solution()
    ans = solution.letterCombinations(test_case)

    explain = """
    In BFS, we can count all paths if we do not use visited memory. And the paths are related to Backtracking.
    """