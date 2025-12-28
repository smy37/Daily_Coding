from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = {}
        for n in nums:
            if n not in num_dict:
                num_dict[n] = 0
            num_dict[n] += 1

        heap = [[-v, k] for k, v in num_dict.items()]
        heapq.heapify(heap)

        while k > 0:
            _, candidate = heapq.heappop(heap)
            answer.append(candidate)
            k -= 1

        return answer


if __name__ == "__main__":
    test_nums = [1,1,1,2,2,3]
    test_k = 2
    sol = Solution()
    print(sol.topKFrequent(test_nums, test_k))

    explain = """
    When finding the k-th element in a list of numbers, the most common approach is sorting.  
    Another approach is to use a heap, since it allows us to efficiently extract the current minimum or maximum value.
    """