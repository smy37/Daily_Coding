class MinStack:
    def __init__(self):
        self.list = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.list.append(val)
        if len(self.min_stack) < 1:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.list.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    val = 5
    obj = MinStack()
    obj.push(val)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    explain = """
    If the values in the stack are kept in ascending or descending order, this becomes the key to solving state-change problems.
    There are two main concepts for maintaining a sorted stack:
    The first is to pop elements that break the ordering.
    The second is to duplicate and store specific values such as the current minimum or maximum.
    """