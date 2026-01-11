from typing import List
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min_v = min(nums)
        # idx_min = nums.index(min_v)
        # rotated_dist = len(nums) - idx_min
        # sorted_nums = nums[idx_min:] + nums[:idx_min]
        # target_idx = bisect_left(sorted_nums, target)
        # if target_idx >= len(nums) or sorted_nums[target_idx] != target:
        #     return -1
        # rotated_target_idx = target_idx - rotated_dist
        #
        # if rotated_target_idx < 0:
        #     return rotated_target_idx + len(nums)
        # else:
        #     return rotated_target_idx

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1






if __name__ == "__main__":
    test_case = [4,5,6,7,0,1,2]
    test_target = 1
    sol = Solution()
    print(sol.search(test_case, test_target))

    explain = """
    First, reconstruct the array by sorting it, then find the target index using binary search.  
    Finally, adjust the index to match the original array index.
    """