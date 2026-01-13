from typing import List

class Solution():
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -float("inf")

        accum_val = 0
        for n in nums:
            if accum_val+n <= n:
                accum_val = n
            else:
                accum_val += n
            answer = max(answer, accum_val)

        return answer



if __name__ == "__main__":
    test_case = [-2,1,-3,4,-1,2,1,-5,4]
    sol = Solution()
    print(sol.maxSubArray(test_case))

    explain = """
    The key idea is to reset the cumulative sum to the current number n 
    if the current cumulative sum is less than n.
    """