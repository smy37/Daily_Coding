from typing import List
from collections import deque

class Solution:
    ## 1. First Approach
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     answer = []
    #     num_candi = set(sorted(candidates))
    #
    #     dq = deque()
    #     dq.append([])
    #     visit = {}
    #     while dq:
    #
    #         cur = dq.popleft()
    #         sum_cur = sum(cur)
    #
    #         for n in num_candi:
    #             temp = sorted(cur + [n])
    #             if tuple(temp) not in visit:
    #                 if sum_cur + n == target:
    #                     if temp not in answer:
    #                         answer.append(temp)
    #                 elif sum_cur + n < target:
    #                     dq.append(cur+[n])
    #                 visit[tuple(temp)] = True
    #
    #     return answer

    ## 2. Second Approach
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        num_candi = set(sorted(candidates))

        dq = deque()
        dq.append([])
        while dq:

            cur = dq.popleft()
            sum_cur = sum(cur)

            if sum_cur == target:
                answer.append(cur)

            for n in num_candi:
                if len(cur) > 0:
                    if cur[-1] <= n and sum_cur+n <=target:
                        dq.append(cur + [n])
                else:
                    if sum_cur+n <= target:
                        dq.append(cur+[n])
        return answer

if __name__ == "__main__":
    t_c = [2,3,6,7]
    t_t = 7
    sol = Solution()
    print(sol.combinationSum(t_c, t_t))

    explain = """
    Combinations can be enumerated using a BFS algorithm.  
    However, the performance is determined by maintaining a decreasing order,  
    which effectively prunes unnecessary branches.
    """