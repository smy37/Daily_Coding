class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for cur_s in s:
            if cur_s in ["(", "{", "["]:
                stack.append(cur_s)
            else:
                if len(stack) == 0:
                    return False
                if cur_s == ")":
                    if stack[-1] != "(":
                        return False
                elif cur_s == "}":
                    if stack[-1] != "{":
                        return False
                elif cur_s == "]":
                    if stack[-1] != "[":
                        return False
                stack.pop()
        if stack:
            return False
        else:
            return True
