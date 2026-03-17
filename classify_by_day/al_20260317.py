from typing import List
import heapq

class Solution:
    ## First Approach. (Too slow)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     answer = []
    #     left = -1
    #     cur_max = -float("inf")
    #
    #     for right in range(k - 1, len(nums)):
    #         n = nums[right]
    #         if right - k + 1 > left:
    #             temp_max = -float("inf")
    #             for i in range(right - k + 1, right + 1):
    #                 if temp_max <= nums[i]:
    #                     temp_max = nums[i]
    #                     left = i
    #             answer.append(temp_max)
    #             cur_max = temp_max
    #         else:
    #             if n >= cur_max:
    #                 left = right
    #                 cur_max = n
    #                 answer.append(n)
    #             else:
    #                 answer.append(nums[left])
    #
    #     return answer


    ## Second Approach (Using heap)
    #     answer = []
    #
    #     heap = []
    #     heapq.heapify(heap)
    #
    #     for idx, n in enumerate(nums):
    #         if len(heap) == 0:
    #             heapq.heappush(heap, [-n, idx])
    #         else:
    #             if heap[0][0] >= -n:
    #                 heap = [[-n, idx]]
    #                 heapq.heapify(heap)
    #             else:
    #                 while len(heap) > 0 and heap[0][1] < idx-k+1:
    #                     heapq.heappop(heap)
    #                 heapq.heappush(heap, [-n, idx])
    #         if idx >= k-1:
    #             answer.append(-heap[0][0])
    #
    #     return answer

    ## Third Approach (Using deque)
        from collections import deque
        answer = []

        dq = deque()
        for idx, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(idx)
            if dq[0] < idx-k +1:
                dq.popleft()

            if idx >= k-1:
                answer.append(nums[dq[0]])
        return answer

if __name__ == "__main__":
    num_list = [1,-1]
    k = 1
    sol = Solution()
    print(sol.maxSlidingWindow(num_list, k))
