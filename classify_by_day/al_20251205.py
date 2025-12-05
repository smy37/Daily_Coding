from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        min_num_l = [float("inf") for _ in range(len(nums))]
        min_num_l[0] = 0
        for i in range(len(nums)):
            for j in range(nums[i]):
                if i + j + 1 >= len(nums):
                    break
                min_num_l[i + j + 1] = min(min_num_l[i + j + 1], min_num_l[i] + 1)

        return min_num_l[-1]


if __name__ == "__main__":
    test_case = [2,3,1,1,4]
    sol = Solution()
    print(sol.jump(test_case))

    explain = """
    Due to the nature of the jumping problem, once we move past the current position, 
    we no longer need to consider it or any previous positions.  
    Therefore, we can simply iterate in order and update the minimum required value at each step.
    """