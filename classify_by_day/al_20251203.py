from typing import List
from collections import deque

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis_l = ["(", ")"]
        dq = deque()
        dq.append([[], []])

        for _ in range(n*2):
            new_dq = deque()
            while dq:
                cur_stack, acc_stack = dq.popleft()
                for p in parenthesis_l:
                    if p == "(":
                        new_dq.append([cur_stack+["("], acc_stack+["("]])
                    elif p == ")":
                        if len(cur_stack)>0 and cur_stack[-1] == "(":
                            cur_stack.pop()
                            new_dq.append([cur_stack, acc_stack+[")"]])
            dq = new_dq
        answer = []
        for c in dq:
            if len(c[0]) ==0:
                answer.append("".join(c[1]))

        return answer

if __name__ == "__main__":
    test_case = 3
    sol = Solution()
    print(sol.generateParenthesis(test_case))

    explain = """
    A tree diagram can be generated using the BFS algorithm.  
    We can prune invalid cases by checking whether the parentheses are correctly paired.
    """
