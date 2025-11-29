from typing import List
from collections import deque

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float("inf") for _ in range(n)] for _ in range(m)]
        dp[0][0] = grid[0][0]
        x_move = [1, 0]
        y_move = [0, 1]

        dq = deque()
        dq.append([0, 0])
        visit = {(0,0): True}

        while dq:
            cur_x, cur_y = dq.popleft()
            for i in range(2):
                next_x, next_y = cur_x + x_move[i], cur_y + y_move[i]
                if 0<= next_x < m and 0<= next_y < n:
                    if (next_x, next_y) not in visit:
                        visit[(next_x, next_y)] = True
                        dq.append([next_x, next_y])
                    dp[next_x][next_y] = min(dp[next_x][next_y], dp[cur_x][cur_y]+grid[next_x][next_y])

        return dp[-1][-1]


if __name__ == "__main__":
    test_case = [[1,2,3],[4,5,6]]
    sol = Solution()
    ans = sol.minPathSum(test_case)
    print(ans)

    explain = """
    A path is considered different if the sequence of nodes it passes through is different. 
    So by skipping visited memory or by using backtracking, we can distinguish all unique paths.
    For this problem, I used BFS since movement is restricted to only down and right, 
    but a double for-loop can also solve it.
    """