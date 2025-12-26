from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        num_l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                num_l.append(matrix[i][j])

        idx = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[j][-(i+1)] = num_l[idx]

                idx += 1
        print(matrix)

if __name__ == "__main__":
    test_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol = Solution()
    sol.rotate(test_matrix)

    explain = """
    Extract number sordered double for-loop and convert original matrix using them.
    """