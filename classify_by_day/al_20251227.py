from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        new_nums = [-n for n in nums]
        heapq.heapify(new_nums)
        cnt = 1
        while cnt <= k:
            num = heapq.heappop(new_nums)
            cnt +=1

        return -num


if __name__ == "__main__":
    test_nums = [3,2,1,5,6,4]
    test_k = 2
    sol = Solution()
    print(sol.findKthLargest(test_nums, test_k))

    explain = """
    The k-th largest element in a list can be found using a heap without sorting.  
    Since Python provides only a min-heap, we can simulate a max-heap by reversing the sign of the numbers.
    """