from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float("inf")
        for i in range(len(nums) - 1, 1, -1):
            left, right = 0, i - 1
            cur = nums[left] + nums[right] + nums[i]
            temp_close = cur
            if cur == target:
                return target
            else:
                while left < right:
                    cur = nums[left] + nums[right] + nums[i]
                    if abs(target - temp_close) > abs(target - cur):
                        temp_close = cur
                    if cur == target:
                        return target
                    elif cur > target:
                        right -=1
                    else:
                        left += 1

            if abs(target - answer) > abs(target - temp_close):
                answer = temp_close
        return answer

sol = Solution()
print(sol.threeSumClosest([0,3,97,102,200], 300))