from typing import List

class Solution:

    ## 1. First Approach
    # def canJump(self, nums: List[int]) -> bool:
    #     cur_idx = 0
    #     visit = {cur_idx: True}
    #     while 0 <= cur_idx < len(nums)-1:
    #         visit[cur_idx] = True
    #         next_idx = cur_idx + nums[cur_idx]
    #         if next_idx <= cur_idx:
    #             while 1:
    #
    #                 next_idx -= 1
    #                 if next_idx not in visit:
    #                     visit[next_idx] = True
    #                     break
    #         cur_idx = next_idx
    #     if cur_idx >= len(nums)-1:
    #         return True
    #     else:
    #         return False
    ## 2. Second Approach
    def canJump(self, nums: List[int]) -> bool:
        cur_reach = 0
        for i in range(len(nums)):
            if i > cur_reach:
                return False
            cur_reach = max(cur_reach, nums[i]+i)
        if cur_reach >= len(nums)-1:
            return True
        else:
            return False

if __name__ == "__main__":
    test_case = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(test_case))

    explain = """
    Update the maximum reachable index and compare it with the current index to check if the position is reachable.
    """