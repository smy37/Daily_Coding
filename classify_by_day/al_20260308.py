from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        ## 1. Brute Force Approach
        # answer = 0
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > 2*nums[j]:
        #             answer += 1
        #
        # return answer

        ## 2. Merge Sort Approach
        global answer
        answer = 0

        def merge_sort(current_array):
            global answer
            if len(current_array) == 1:
                return current_array

            left, right = 0, len(current_array)-1
            mid = (left+right)//2

            left_array, right_array = merge_sort(current_array[:mid+1]), merge_sort(current_array[mid+1:])

            temp = []
            idx_left, idx_right = 0, 0

            while idx_left < len(left_array) and idx_right < len(right_array):
                if left_array[idx_left] <= 2* right_array[idx_right]:
                    idx_left += 1
                else:
                    answer += len(left_array)-idx_left
                    idx_right += 1

            idx_left, idx_right = 0, 0
            while idx_left < len(left_array) and idx_right < len(right_array):
                if left_array[idx_left] <= right_array[idx_right]:
                    temp.append(left_array[idx_left])
                    idx_left += 1
                else:
                    temp.append(right_array[idx_right])
                    idx_right += 1
            temp.extend(left_array[idx_left:])
            temp.extend(right_array[idx_right:])

            return temp
nums = [2,4,3,5,1]
sol = Solution()
sol.reversePairs(nums)