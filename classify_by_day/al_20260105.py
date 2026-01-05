from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        cp = Counter(p)
        len_s, len_p = len(s), len(p)

        for i in range(len_s-len_p+1):
            temp_cnt = Counter(s[i:i+len_p])
            if temp_cnt == cp:
                answer.append(i)
        return answer


if __name__ == "__main__":
    test_s, test_p = "cbaebabacd", "abc"
    sol = Solution()
    sol.findAnagrams(test_s, test_p)