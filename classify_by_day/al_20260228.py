from typing import List
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum = [0]
        even_sum = [0]

        for i in range(len(nums)):
            if i % 2 == 0:
                even_sum.append(even_sum[-1] + nums[i])
            else:
                odd_sum.append(odd_sum[-1] + nums[i])

        answer = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                cri = i//2 + 1
                even = even_sum[cri-1] + odd_sum[-1]-odd_sum[cri-1]
                odd = even_sum[-1]-even_sum[cri] + odd_sum[cri-1]
            else:
                cri = i//2 + 1
                even = even_sum[cri] + odd_sum[-1] - odd_sum[cri]
                odd = odd_sum[cri-1] + even_sum[-1] - even_sum[cri]
            if even == odd:
                answer += 1
        return answer

sol = Solution()
sol.waysToMakeFair([2, 1, 6, 4, 3, 3])