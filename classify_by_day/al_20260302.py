from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        ## First Approach
        # n = len(nums)
        # for i in range(n):
        #     for j in range(n-i-1):
        #         if nums[j] > nums[j+1]:
        #             memory = nums[j+1]
        #             nums[j+1] = nums[j]
        #             nums[j] = memory
        # return nums

        ## Second Approach

        def qsort(num_list: List[int]):
            if len(num_list) < 2:
                return num_list

            pivot = random.choice(num_list)
            less = []
            great = []
            equal = []
            for n in num_list:
                if n < pivot:
                    less.append(n)
                elif n > pivot:
                    great.append(n)
                else:
                    equal.append(n)

            return qsort(less) + equal + qsort(great)

        nums = qsort(nums)

        return nums


explain = """
Implementing quick sort using divide and conquer.
"""