from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:{} for i in range(numCourses)}
        visit = {}
        dq = deque()
        for after, pre in prerequisites:
            graph[after][pre] = True
            if after in graph[pre]:
                return False

        for num in graph:
            if num not in visit:
                visit[num] = True
                dq.append(num)

                while dq:
                    cur = dq.popleft()

                    for next_num in graph[cur]:
                        if next_num not in visit:
                            visit[next_num] = True
                            dq.append(next_num)

        if len(visit) == numCourses or len(prerequisites) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(3, [[1,0],[0,2],[2,1]]))
