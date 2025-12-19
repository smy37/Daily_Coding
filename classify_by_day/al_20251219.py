from typing import List

class Solution:
    def dfs(self, stack, visit, num_list, global_path):
        cur = stack.pop()

        for num in num_list:
            if num not in visit:
                temp = tuple(sorted(cur+[num]))
                if temp not in global_path:

                    global_path[temp] = True
                    visit[num] = True
                    self.dfs([cur+[num]], visit, num_list, global_path)
                    del visit[num]


    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = [[]]
        global_visit = {(): True}
        v_dict = {}
        self.dfs(s, v_dict, nums, global_visit)
        return [list(item) for item in global_visit.keys()]


if __name__ == "__main__":
    test_case = [1,2,3]
    sol = Solution()
    print(sol.subsets(test_case))
    explain = """
    When traversing combination paths, a visited dictionary is needed if duplicate numbers exist.  
    By sorting each combination and storing it in a global visited memory, we can detect and avoid duplicate paths.
    """

