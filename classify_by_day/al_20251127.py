class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = ""
        for i in range(len(s)):
            if s[i] == "[":
                stack.append(int(k))
                k = ""
                stack.append("[")
            elif s[i] == "]":
                b_string = ""
                while stack[-1] != "[":
                    b_string = stack.pop() + b_string
                stack.pop()
                num = stack.pop()
                stack.append(b_string*num)
            else:
                if s[i].isdigit():
                    k += s[i]
                else:
                    stack.append(s[i])

        ans = "".join(stack)
        return ans


if __name__ =="__main__":
    sol = Solution()
    test = "2[abc]3[cd]ef"
    print(sol.decodeString(test))

    explain ="""
    A common use case of a stack is simulation.
    We keep an order in the stack using pop(), 
    and this order is used to carry out the simulation.
    """