import sys

iter_num = int(sys.stdin.readline())

class Stack:
    def __init__(self):
        self.cont = []

    def push(self,x):
        self.cont.append(x)

    def pop(self):
        if len(self.cont) != 0:
            print(self.cont.pop())
        else:
            print(-1)

    def size(self):
        print(len(self.cont))

    def empty(self):
        if len(self.cont) !=0 :
            print(0)
        else:
            print(1)

    def top(self):
        if len(self.cont) != 0:
            print(self.cont[-1])
        else:
            print(-1)


temp_s = Stack()
for i in range(iter_num):
    temp = sys.stdin.readline().rstrip().split()

    if temp[0] == 'push':
        temp_s.push(temp[1])
    elif temp[0] == 'pop':
        temp_s.pop()
    elif temp[0] == 'size':
        temp_s.size()
    elif temp[0] == 'empty':
        temp_s.empty()
    elif temp[0] == 'top':
        temp_s.top()
