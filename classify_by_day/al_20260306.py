from typing import List

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        left = self.beautifulArray((n+1) // 2)
        for i in range(len(left)):
            left[i] = 2 * left[i] - 1

        right = self.beautifulArray(n // 2)
        for i in range(left(right)):
            right[i] = 2 * left[i]

        return left + right

sol = Solution()
sol.beautifulArray(4)