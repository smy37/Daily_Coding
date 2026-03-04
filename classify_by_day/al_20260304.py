from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        answer = -float("inf")
        answer_idx = 0
        while left <= right:
            mid = (left + right) // 2
            if answer < arr[mid]:
                answer_idx = mid
                answer = arr[mid]

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid - 1
        return answer_idx


if __name__ == "__main__":
    arr = [0, 10, 5, 2]
    sol = Solution()
    print(sol.peakIndexInMountainArray(arr))

explain="Finding maximum value in array using binary search"