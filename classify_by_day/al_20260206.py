class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        cur_min = float("inf")
        for p in prices:
            answer = max(answer, p-cur_min)
            cur_min = min(cur_min, p)
        return answer
