from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        accum_sum = 0
        accum_dict = {}
        accum_dict[0] = 1
        for n in nums:
            accum_sum += n

            if accum_sum - k in accum_dict:
                cnt += accum_dict[accum_sum-k]

            if accum_sum not in accum_dict:
                accum_dict[accum_sum] = 0
            accum_dict[accum_sum] += 1
            print(n, accum_dict)
        return cnt

if __name__ == "__main__":
    test_nums = [100, 100, 1, 1, 1, 1, 1]
    sol = Solution()
    print(sol.subarraySum(test_nums, 5))

    explain = """
    This problem can be solved by reverse thinking with prefix sums.  
    The key idea is to subtract the target value from the current prefix sum 
    and check whether the resulting value exists in memory.
    """