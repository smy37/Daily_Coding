from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length = len(matrix)*len(matrix[0])
        dx_l = [0, 1, 0, -1]
        dy_l = [1, 0, -1, 0]

        cur_x, cur_y = 0, 0
        visit = {(0,0): True}
        answer = [matrix[0][0]]

        idx = 0
        while len(answer) < length:
            next_x, next_y = cur_x+dx_l[idx], cur_y+dy_l[idx]

            if (next_x, next_y) not in visit and (0<=next_x<len(matrix) and 0<=next_y<len(matrix[0])):
                visit[(next_x, next_y)] = True
                answer.append(matrix[next_x][next_y])
                cur_x = next_x
                cur_y = next_y
            else:
                idx = idx+1 if idx != 3 else 0

        return answer


if __name__ == "__main__":
    test_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print(sol.spiralOrder(test_matrix))