from typing import List

def dfs(stack, path, visit, graph):
    cur = stack.pop()
    ans = True
    for next_node in graph[cur]:
        if next_node in path:
            return False
        if next_node not in visit:
            visit[next_node] = True
            path[next_node] = True
            ans = dfs(stack + [next_node], path, visit, graph)
            del path[next_node]
            if not ans:
                break
    return ans

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = {}
        graph = {}
        for i in range(numCourses):
            graph[i] = {}

        for after, pre in prerequisites:
            graph[after][pre] = True

        for num in graph:
            if num not in visit:
                answer = dfs([num], {num: True}, visit, graph)

                if not answer:
                    return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(4,[[0,1],[3,1],[1,3],[3,2]]))

    explain = """
    To determine whether a cycle exists in a graph, we can use either a disjoint set or a DFS algorithm. 
    It is important to consider whether the graph is directed or undirected, because the way we detect cycles depends on this.
    In directed graphs, visited memory is used for pruning, and path memory is used to detect cycles.
    """