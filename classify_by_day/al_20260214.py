class MyQueue:

    def __init__(self):
        self.memory = []
        self.idx = 0

    def push(self, x: int) -> None:
        self.memory.append(x)

    def pop(self) -> int:
        if self.memory and self.idx < len(self.memory):
            value = self.memory[self.idx]
            self.idx += 1
            return value

    def peek(self) -> int:
        if self.memory and self.idx < len(self.memory):
            return self.memory[self.idx]

    def empty(self) -> bool:
        if self.memory and self.idx < len(self.memory):
            return False
        else:
            return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

explain ="""
Implement of queue using stack and index.
"""