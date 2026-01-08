from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_idx = {}
        without_zero = 1
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                zero_idx[i] = True
            else:
                without_zero *= n
        if len(zero_idx) > 1:
            return [0 for _ in range(len(nums))]
        elif len(zero_idx) == 1:
            answer = [0 for _ in range(len(nums))]
            for i in zero_idx:
                answer[i] = without_zero
            return answer
        else:
            answer = []
            for i in range(len(nums)):
                n = nums[i]
                answer.append(without_zero//n)
            return answer


if __name__ == "__main__":
    test_nums = [1,2,3,4]
    sol = Solution()
    print(sol.productExceptSelf(test_nums))
