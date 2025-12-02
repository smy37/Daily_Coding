from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        move_x = [1, -1, 0, 0]
        move_y = [0, 0, -1, 1]

        dq = deque()
        visit = {}

        fresh_cnt = 0
        rotten_cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_cnt += 1
                elif grid[i][j] == 2:
                    rotten_cnt += 1
                    dq.append([i, j, 0])
                    visit[(i, j)] = True
        if fresh_cnt == 0:
            return 0

        while dq:
            cur_x, cur_y, time = dq.popleft()
            for i in range(4):
                next_x, next_y = cur_x+move_x[i], cur_y+move_y[i]
                if 0<=next_x<m and 0<=next_y<n and (next_x, next_y) not in visit:
                    visit[(next_x, next_y)] = True
                    if grid[next_x][next_y] == 1:
                        fresh_cnt -= 1
                        grid[next_x][next_y] = 2
                        dq.append([next_x, next_y, time+1])
                        if fresh_cnt == 0:
                            return time+1

        return -1


if __name__ == "__main__":
    test_case = [[0,2]]
    sol = Solution()
    print(sol.orangesRotting(test_case))

    explain = """
    Add all starting points to the deque and apply BFS. 
    When the deque contains multiple starting points, 
    this effectively handles the multi-source BFS problem.
    """