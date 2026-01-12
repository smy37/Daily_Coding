from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_value = float("inf")
        left, right = 0, len(nums)-1

        while left<=right:
            mid = (left+right)//2
            min_value = min(min_value, nums[mid])

            if nums[left] <= nums[mid]:
                if nums[mid] <= nums[right]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                right = mid-1
        return min_value

if __name__ == "__main__":
    test_case = [3,4,5,1,2]
    sol = Solution()
    print(sol.findMin(test_case))
    explain = """
    Apply binary search on semi-sorted array.
    """
