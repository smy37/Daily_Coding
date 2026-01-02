from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col_dict = {}
        for i in range(len(matrix)):
            flag = False
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    col_dict[j] = True
                    flag = True
            if flag:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        for c in col_dict:
            for i in range(len(matrix)):
                matrix[i][c] = 0


if __name__ == "__main__":
    test_matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    sol.setZeroes(test_matrix)

    explain = """
    Iterate through the matrix using a double for-loop.  
    First, record the column indices that need to be set to zero.  
    Second, set all elements in the corresponding rows to zero.  
    Third, set all elements in the recorded columns to zero.
    """