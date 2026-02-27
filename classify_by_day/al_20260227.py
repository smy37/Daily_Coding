from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        mod = total_sum % p
        if mod == 0:
            return 0

        answer = len(nums)

        memory = {0:-1}
        cur_sum = 0

        for idx, n in enumerate(nums):
            cur_sum += n
            temp_mod = cur_sum%p
            target = temp_mod-mod if temp_mod-mod >= 0 else temp_mod-mod + p
            if target in memory:
                answer = min(answer, idx - memory[target])
            memory[temp_mod] = idx

        if answer == len(nums):
            return -1
        else:
            return answer

sol = Solution()
print(sol.minSubarray([8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2], 148))