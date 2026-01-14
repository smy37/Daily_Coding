from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        answer_left, answer_right = len(nums), -1

        ## Find LeftSide
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer_left = min(answer_left, mid)

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        ## Find RightSide
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                answer_right = max(answer_right, mid)

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if answer_left == len(nums):
            answer_left = -1

        return [answer_left, answer_right]


if __name__ == "__main__":
    sol = Solution()
    nums = []
    target = 0
    print(sol.searchRange(nums, target))

    explain = """
    Use two binary searches to find the leftmost and rightmost indices of the target.
    """