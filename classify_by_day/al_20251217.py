from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp


if __name__ == "__main__":
    test_case = [2,0,2,1,1,0]
    sol = Solution()
    sol.sortColors(test_case)
    print(test_case)

    explain = """
    The list is sorted using bubble sort.  
    Since a list is mutable, its elements can be modified using assignments like nums[i] = new_value.  
    This is different from rebinding the variable itself, such as nums = new_object.
    """