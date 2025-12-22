from typing import List

def find(x, parent_dict: dict):
    parent = parent_dict[x]

    if x != parent:
        parent = find(parent, parent_dict)

    parent_dict[x] = parent

    return parent

def union(x, y, parent_dict):
    parent_x = find(x, parent_dict)
    parent_y = find(y, parent_dict)

    if parent_x <= parent_y:
        parent_dict[parent_y] = parent_x
    else:
        parent_dict[parent_x] = parent_y


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     parent_d = {n : n for n in nums}
    #     score = {n: 0 for n in nums}
    #     visit = {}
    #     for n in nums:
    #         if n not in visit:
    #             visit[n] = True
    #             if n+1 in visit:
    #                 union(n, n+1, parent_d)
    #             if n-1 in visit:
    #                 union(n, n-1, parent_d)
    #
    #     for key, value in parent_d.items():
    #         parent = find(value, parent_d)
    #         score[parent] += 1
    #     return max(score.values())

    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        set_num = set(nums)

        for n in set_num:
            if n-1 not in set_num:
                start = n
                while start in set_num:
                    start += 1
                answer = max(answer, start-n)
        return answer
if __name__ == "__main__":
    test_case = [0,3,7,2,5,8,4,6,0,1]
    sol = Solution()
    print(sol.longestConsecutive(test_case))


    explain = """
    A set behaves like a dictionary, so lookup operations run in O(1) time.  
    """