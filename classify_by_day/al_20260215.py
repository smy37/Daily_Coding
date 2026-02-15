import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minus_stone = [-s for s in stones]
        heapq.heapify(minus_stone)
        while minus_stone:
            y = heapq.heappop(minus_stone)
            if minus_stone:
                x = heapq.heappop(minus_stone)
                if -y > -x:
                    heapq.heappush(minus_stone, y-x)

            else:
                return -y
        return 0
