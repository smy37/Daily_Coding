class Solution:
    def longestValidParentheses(self, s: str) -> int:
        memory = [0 for _ in range(len(s)+1)]
        stack = []

        for idx, p in enumerate(s):
            if not stack:
                if p == "(":
                    stack.append(["(", idx])
            else:
                if p == "(":
                    stack.append(["(", idx])
                elif p == ")":
                    if stack[-1][0] == "(":

                        _, start_idx = stack.pop()
                        memory[idx+1] = memory[start_idx] + memory[idx] + 2

                    else:
                        stack = []
        return max(memory)

    ## First Approach
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = []
    #     answer = 0
    #     temp = 0
    #     for idx, p in enumerate(s):
    #         if not stack:
    #             if p == "(":
    #                 stack.append("(")
    #         else:
    #             if p == "(":
    #                 stack.append("(")
    #             elif p == ")":
    #                 if stack[-1] == "(":
    #                     temp += 2
    #                     answer = max(answer, temp)
    #                     stack.pop()
    #                 else:
    #                     stack = []
    #                     temp = 0
    #     return answer


sol = Solution()
sol.longestValidParentheses(")()(())()")