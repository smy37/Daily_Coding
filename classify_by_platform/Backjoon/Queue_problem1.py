import sys

class Queue():

    def __init__(self):
        self.cont = []
        self.cnt = 0

    def push(self,x):
        self.cont.append(x)

    def pop(self):
        if len(self.cont) == self.cnt:
            print(-1)
        else:
            print(self.cont[self.cnt])
            self.cnt += 1
    def size(self):
        print(len(self.cont)-self.cnt)

    def empty(self):
        tem = len(self.cont)-self.cnt
        if tem == 0:
            print(1)
        else: print(0)
    def front(self):
        tem = len(self.cont)-self.cnt
        if tem == 0:
            print(-1)
        else:
            print(self.cont[self.cnt])

    def back(self):
        tem = len(self.cont)-self.cnt
        if tem == 0:
            print(-1)
        else:
            print(self.cont[-1])

que = Queue()
iter_num = int(sys.stdin.readline())

for i in range(iter_num):
    temp = list(sys.stdin.readline().split())

    if temp[0] == 'push':
        que.push(temp[1])

    elif temp[0] == 'pop':
        que.pop()

    elif temp[0] == 'size':
        que.size()

    elif temp[0] == 'empty':
        que.empty()

    elif temp[0] == 'front':
        que.front()

    elif temp[0] == 'back':
        que.back()