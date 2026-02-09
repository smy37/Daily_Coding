class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "/", "*"]:
                right = stack.pop()
                left = stack.pop()
                value = int(eval(f"{left}{token}{right}"))
                stack.append(value)
            else:
                stack.append(token)
        return int(stack[-1])