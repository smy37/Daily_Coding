from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memory = {}
        cri = len(nums)//2
        for n in nums:
            if n not in memory:
                memory[n] = 0
            memory[n] += 1

        answer = 0

        for n in memory:
            if memory[n] > cri:
                answer= n
                break
        
        return answer


if __name__ == "__main__":
    test = [3,2,3]
    sol = Solution()
    sol.majorityElement(test)
