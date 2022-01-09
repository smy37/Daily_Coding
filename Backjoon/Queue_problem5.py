import sys

class Deque():
    def __init__(self):
        self.cont = []

    def push_front(self, x):
        self.cont = [x] + self.cont

    def push_back(self, x):
        self.cont.append(x)

    def pop_front(self):
        try:
            print(self.cont[0])
            self.cont = self.cont[1:]
        except:
            print(-1)

    def pop_back(self):
        try:
            print(self.cont.pop())
        except:
            print(-1)
    def deque_size(self):
        print(len(self.cont))

    def deque_empty(self):
        if len(self.cont) == 0:
            print(1)
        else:
            print(0)
    def front(self):
        try:
            print(self.cont[0])
        except:
            print(-1)

    def back(self):
        try:
            print(self.cont[-1])
        except:
            print(-1)

dq = Deque()

iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    temp = list(sys.stdin.readline().strip().split())

    if temp[0] == 'push_front':
        dq.push_front(temp[1])
    elif temp[0] == 'push_back':
        dq.push_back(temp[1])
    elif temp[0] == 'pop_front':
        dq.pop_front()
    elif temp[0] == 'pop_back':
        dq.pop_back()
    elif temp[0] == 'size':
        dq.deque_size()
    elif temp[0] == 'empty':
        dq.deque_empty()
    elif temp[0] == 'front':
        dq.front()
    elif temp[0] == 'back':
        dq.back()
