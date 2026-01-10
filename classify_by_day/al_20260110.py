from typing import List
from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        one_array = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
        idx = bisect_left(one_array, target)

        if idx < m*n:
            if one_array[idx] == target:
                return True

        return False


if __name__ == "__main__":
    test_case = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    test_target = 3
    sol = Solution()
    print(sol.searchMatrix(test_case, test_target))

