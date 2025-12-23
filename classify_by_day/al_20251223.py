from typing import List

class Solution:
    ## First Approach
    # def canPartition(self, nums: List[int]) -> bool:
    #     answer = False
    #     nums = sorted(nums)
    #     total_sum = sum(nums)
    #     cur_sum = 0
    #     for n in nums:
    #         cur_sum += n
    #         diff = total_sum - cur_sum
    #         if cur_sum > diff:
    #             break
    #         elif cur_sum == diff:
    #             answer = True
    #             break
    #     return answer

    ## Second Approach
    # def canPartition(self, nums: List[int]) -> bool:
    #     nums = sorted(nums)
    #     total_sum = sum(nums)
    #     n = len(nums)
    #     dp = [0 for _ in range(n+1)]
    #
    #     for i in range(1, n+1):
    #         dp[i] = dp[i-1] + nums[i-1]
    #
    #     for i in range(1, n+1):
    #         for j in range(i, n+1):
    #             i_j_sum = dp[j]-dp[i-1]
    #             diff = total_sum - i_j_sum
    #             if diff == i_j_sum:
    #                 return True
    #     return False

    ## Third Approach
    # def dfs(self, cur, visit, memory, num_list, target):
    #     global flag
    #     if sum(cur) == target:
    #         return True
    #
    #     for i, n in enumerate(num_list):
    #         if i not in visit:
    #             temp = tuple(sorted(cur + [n]))
    #             if temp not in memory:
    #                 memory[temp] = True
    #                 visit[i] = True
    #                 temp_flag = self.dfs(cur + [n], visit, memory, num_list, target)
    #                 del visit[i]
    #
    #                 if temp_flag:
    #
    #                     flag = True
    #                     break
    #
    # def canPartition(self, nums: List[int]) -> bool:
    #     global flag
    #     flag = False
    #     nums = sorted(nums)
    #     t = sum(nums)//2
    #     if t != sum(nums)/2:
    #         return False
    #     m = {}
    #     v = {(): True}
    #     s = []
    #
    #     self.dfs(s, v, m, nums, t)
    #     return flag

    ## Fourth Approach


    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False

        target = sum(nums)//2
        sum_dict = {(0, 0): True}
        current_sum = 0

        def dfs(idx, cur_sum):
            flag = False
            if target == cur_sum:
                return True

            if cur_sum > target or idx >= len(nums):
                return False

            if (idx+1, cur_sum+nums[idx]) not in sum_dict:
                sum_dict[(idx+1, cur_sum+nums[idx])] = True
                flag = dfs(idx + 1, cur_sum + nums[idx])
                if flag: return True
            if (idx+1, cur_sum) not in sum_dict:
                sum_dict[(idx+1, cur_sum)] = True
                flag = dfs(idx + 1, cur_sum)
                if flag: return True
            return flag


        answer = dfs(0, current_sum)
        if not answer:
            answer = False

        return answer




if __name__ == "__main__":
    test_case_l = [[23,13,11,7,6,5,5]]
    sol = Solution()
    for nums in test_case_l:
        test_answer = sol.canPartition(nums)
        print(test_answer)

    explain = """
    Consecutive property of subset is not necessary. And just tree traversal is enough not graph traversal.  
    """