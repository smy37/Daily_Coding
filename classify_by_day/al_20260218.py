from typing import List

import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0] == 1

        minus_l = [-n for n in target]

        heapq.heapify(minus_l)

        while sum(minus_l) != -len(minus_l):
            max_v = heapq.heappop(minus_l)
            cur_sum = sum(minus_l)

            if cur_sum <= max_v:
                return False
            next_v = -max_v % (-cur_sum)
            if next_v == 0:
                if cur_sum != -1:
                    return False
                heapq.heappush(minus_l, -1)
            else:
                heapq.heappush(minus_l, -next_v)

        return True



sol = Solution()
print(sol.isPossible([8, 5]))