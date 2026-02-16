from typing import List
import heapq
from collections import deque


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ## First Approach
        # answer = []
        # dq1 = deque(nums1)
        # dq2 = deque(nums2)
        # q1 = dq1.popleft()
        # q2 = dq2.popleft()
        # answer.append([q1, q2])
        # for _ in range(k - 1):
        #     new_q1 = dq1.popleft()
        #     new_q2 = dq2.popleft()
        #
        #     if q1 + new_q2 <= new_q1 + q2:
        #         answer.append([q1, new_q2])
        #         dq1.appendleft(new_q1)
        #         q2 = new_q2
        #
        #     else:
        #         answer.append([new_q1, q2])
        #         dq2.appendleft(new_q2)
        #         q1 = new_q1

        ## Second Approach
        # answer = []
        # heap = []
        # for n1 in nums1:
        #     for n2 in nums2:
        #         heapq.heappush(heap, [n1 + n2, n1, n2])
        # for _ in range(k):
        #     sum_v, v1, v2 = heapq.heappop(heap)
        #     answer.append([v1, v2])

        ## Third Approach
        answer = []
        heap = []
        for i in range(min(k, len(nums2))):
            heapq.heappush(heap, [nums1[0]+nums2[i], 0, i])

        while len(answer) < k:
            _, idx_1, idx_2 = heapq.heappop(heap)
            answer.append([idx_1, idx_2])

            if idx_1 + 1 < len(nums1):
                heapq.heappush(heap, [nums1[idx_1+1]+nums2[idx_2], idx_1+1, idx_2])

        return answer


explain = """
This problem requires a change in perspective.  
Instead of pushing all possible combinations from the two arrays into the heap, 
we fix one array element and only push up to k candidate pairs into the heap.
Initially, we fix the first element of one array and pair it with elements from the other array, 
pushing at most k elements into the heap.  
Then, whenever the minimum element is extracted from the heap, 
we update the index of the corresponding array and push the next candidate into the heap.
"""