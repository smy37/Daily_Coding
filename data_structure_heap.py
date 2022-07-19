import math

class Heap():
    def __init__(self):
        self.array = []

    def add(self, a:int):
        self.array.append(a)
        cur = len(self.array)-1
        while (cur-1)//2 >=0 and self.array[(cur-1)//2]>=self.array[cur]:
            temp = int(self.array[(cur-1)//2])
            self.array[(cur-1)//2] = self.array[cur]
            self.array[cur] = temp
            cur = (cur-1)//2
        print(self.array)
        return

    def delete(self):
        if len(self.array) == 1:
            self.array = []
            return
        self.array = [self.array[-1]] + self.array[1:-1]
        cur = 0

        while (cur < len(self.array) and cur*2+2 <len(self.array)) and (self.array[(cur*2+1)] < self.array[cur] or self.array[cur*2+2] < self.array[cur]):
            if self.array[(cur)*2+1] <= self.array[cur*2+2]:
                temp = int(self.array[cur*2+1])
                self.array[cur*2+1] = self.array[cur]
                self.array[cur] = temp
                cur = cur*2+1
            else:
                temp = int(self.array[cur*2+2])
                self.array[cur*2+2] = self.array[cur]
                self.array[cur] = temp
                cur = cur*2+2
        if len(self.array) == 2:
            self.array = sorted(self.array)
        return


h = Heap()
test = [5, 8, 9, 10, 4, 3, 11, 2, 4]

for i in test:
    h.add(i)
print('#######')
for i in range(9):
    h.delete()
    print(h.array)
