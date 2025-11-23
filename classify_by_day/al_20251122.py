from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m_r = [1, -1, 0, 0]
        m_c = [0, 0, -1, 1]
        M = len(grid)
        N = len(grid[0])
        ans = 0
        visit = {}

        for r in range(M):
            for c in range(N):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dq = deque()
                    dq.append([r,c])
                    visit[(r,c)] = True
                    ans +=1

                    while dq:
                        cur_x, cur_y = dq.popleft()
                        for i in range(4):
                            next_x, next_y = cur_x + m_r[i], cur_y + m_c[i]

                            if 0<=next_x<M and 0<=next_y<N and (next_x, next_y) not in visit and grid[next_x][next_y] == "1":
                                visit[(next_x, next_y)] = True
                                dq.append([next_x, next_y])

        return ans



if __name__ == "__main__":
    test_case = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    sol = Solution()
    print(sol.numIslands(test_case))

    explain = """
    This is a classic problem that can be solved using the BFS Algorithm.
    """