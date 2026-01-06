from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        stack = []

        for inter in intervals:
            print(inter)
            if len(stack) == 0:
                stack.append(inter)
            else:
                if inter[0] > stack[-1][1]:
                    stack.append(inter)
                else:
                    stack[-1][1] = max(stack[-1][1], inter[1])

        return stack


if __name__ == "__main__":
    test_intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(test_intervals))