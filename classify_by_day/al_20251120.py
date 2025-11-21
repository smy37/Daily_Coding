from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## 1. First Approach
        # for i in range(len(heights)):
        #     h = heights[i]
        #
        #     t1 = 0
        #     for j in range(i, -1, -1):
        #         if h > heights[j]:
        #             t1 = (i - j) * h
        #             break
        #     else:
        #         t1 = (i + 1) * h
        #
        #     t2 = 0
        #     for j in range(i, len(heights)):
        #         if h > heights[j]:
        #             t2 = (j - i) * h
        #             break
        #     else:
        #         t2 = (len(heights) - i) * h
        #
        #     answer = max(answer, t1+t2-h)

        ## 2. Second Approach
        # stack = []
        # for i in range(len(heights)):
        #     h = heights[i]
        #     if len(stack) == 0:
        #         stack.append([h, i])
        #         answer = max(answer, h)
        #
        #     else:
        #         t = -1
        #         while stack and h < stack[-1][0]:
        #             th, tt = stack.pop()
        #             t = tt
        #         for pre_h, idx in stack:
        #             answer = max(answer, (i-idx+1)*pre_h)
        #         if t == -1:
        #             if stack[-1][0] < h:
        #                 stack.append([h, i])
        #             answer = max(answer, h*1)
        #         else:
        #             stack.append([h, t])
        #             answer = max(answer, h*(i-t+1))


        ## 3. Third Approach
        answer = 0
        stack = []
        for i in range(len(heights)):
            h = heights[i]
            t = i
            while stack and h < stack[-1][0]:
                t_h, t_i = stack.pop()
                answer = max(answer, (i-t_i)*t_h)
                t = t_i
            stack.append([h, t])
        while stack:
            t_h, t_i = stack.pop()
            answer = max(answer, (len(heights)-t_i)*t_h)
        return answer



if __name__ == "__main__":
    sol = Solution()
    test_heights = [1,1,1,1,1,1,1]

    print(sol.largestRectangleArea(test_heights))

    explain = """
    It is important to understand that if the new height is smaller than the height at the top of the stack,
    we no longer need to consider rectangles using that height.
    At this point, we calculate the area using that height to finalize its contribution.
    """
