# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums)-1
#
#         while left<=right:
#             mid = (left+right)//2
#
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] < target:
#                 left = mid+1
#             elif nums[mid] > target:
#                 right = mid-1
#
#         return -1

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(c**0.5), -1, -1):
            rest = c-i**2
            if int(rest**0.5)**2 == rest:
                return True
        return False

