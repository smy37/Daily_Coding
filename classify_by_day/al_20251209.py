from typing import List
from itertools import permutations

class Solution:
    ## Method 1
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     permu = list(permutations(nums, len(nums)))
    #     return permu

    ## Method 2
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     answer = []
    #     stack = []
    #     def dfs(s):
    #         if len(s) == len(nums):
    #             answer.append(s[:])
    #             return
    #         for n in nums:
    #             if n not in s:
    #                 s.append(n)
    #                 dfs(s)
    #                 s.pop()
    #     dfs(stack)
    #     return answer

    ## Method 3
    def permute(self, nums: List[int]) -> List[List[int]]:
        from collections import deque
        answer = []
        dq = deque()
        dq.append([])
        while dq:
            cur = dq.popleft()
            if len(cur) == len(nums):
                answer.append(cur)
                continue
            for n in nums:
                if n not in cur:
                    dq.append(cur+[n])
        return answer
if __name__ == "__main__":
    test_case = [1, 2, 3]
    sol = Solution()
    print(sol.permute(test_case))

    explain = """
    Using DFS & BFS for backtracking.
    """


