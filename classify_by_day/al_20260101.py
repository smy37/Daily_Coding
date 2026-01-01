from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = i+1
            e = len(nums)-1
            while s < e:
                if nums[i]+nums[s]+nums[e] == 0:
                    answer.add((nums[i], nums[s], nums[e]))
                    s += 1
                elif nums[i]+nums[s]+nums[e] < 0:
                    s += 1
                elif nums[i]+nums[s]+nums[e] > 0:
                    e -= 1

        return [list(item) for item in answer]


if __name__ == "__main__":
    test_num = [-1,0,1,2,-1,-4]
    sol = Solution()
    print(sol.threeSum(test_num))

    explain = """
    When using three pointers in an array, the first pointer is fixed by a for-loop.  
    The second and third pointers are initialized at both ends of the remaining subarray.
    """