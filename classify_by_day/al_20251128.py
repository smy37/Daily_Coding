from collections import deque

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visit = {}
        dq = deque()
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        m_x = [1, 0]
        m_y = [0, 1]
        dq.append([0,0])
        visit[(0,0)] = True
        while dq:
            cur_x, cur_y = dq.popleft()
            for k in range(2):
                next_x, next_y = cur_x+m_x[k], cur_y+m_y[k]

                if 0<=next_x<m and 0<=next_y<n:
                    if (next_x, next_y) not in visit:
                        dq.append([next_x, next_y])
                        visit[(next_x, next_y)] = True
                    dp[next_x][next_y] += dp[cur_x][cur_y]

        return dp[-1][-1]

if __name__ == "__main__":
    m, n = 3, 7
    solution = Solution()
    solution.uniquePaths(m, n)

    explain = """
    Add the coordinate to the stack when the location is not visited, 
    but always add or update the value in memory even if the location is already visited.
    """
