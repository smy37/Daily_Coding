## Problem 1.
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)

        answer = []
        cur = float("inf")

        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < cur:
                cur = arr[i+1]-arr[i]
                answer = [[arr[i], arr[i+1]]]
            elif arr[i+1]-arr[i] == cur:
                answer.append([arr[i], arr[i+1]])
        return answer


## Problem 2.
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)

        answer = 0
        cur = 0
        cur_max = nums[0]
        for i in range(len(nums)):
            if cur_max > nums[i]:
                answer += cur
                cur_max = nums[i]
            cur += 1
        return answer
    