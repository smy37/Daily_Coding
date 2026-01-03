from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        if m <= n:
            for i in range(m):
                if matrix[i][i] == target:
                    return True
                elif matrix[i][i] > target:
                    for j in range(i):
                        for k in range(i, n):
                            if matrix[j][k] == target:
                                return True
                    for j in range(i):
                        for k in range(i, m):
                            if matrix[k][j] == target:
                                return True

            else:
                for j in range(m, n):
                    for k in range(m):
                        if matrix[k][j] == target:
                            return True
        else:
            print('oleh')
            for i in range(n):
                if matrix[i][i] == target:
                    return True
                elif matrix[i][i] > target:
                    print(i)
                    for j in range(i):
                        for k in range(i, m):
                            if matrix[k][j] == target:
                                return True
                    for j in range(i):
                        for k in range(i, n):
                            if matrix[j][k] == target:
                                return True
            else:
                for j in range(n, m):
                    for k in range(n):
                        if matrix[j][k] == target:
                            return True

        return False



if __name__ == "__main__":
    test_matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22]]
    test_target = 15
    sol = Solution()
    print(sol.searchMatrix(test_matrix, test_target))