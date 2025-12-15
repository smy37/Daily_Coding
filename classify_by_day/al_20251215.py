from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        cri = k%n
        right_end = n-cri
        nums[:] = nums[right_end:]+nums[:right_end]



if __name__ == "__main__":
    t_nums = [-1,-100,3,99]
    t_k = 2

    sol = Solution()
    print(sol.rotate(t_nums, t_k))

    explain = """
    When an argument is passed to a function, it is copied. 
    Therefore, modifying the copied value inside the function does not affect the original object.
    """