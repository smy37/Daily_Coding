import heapq

class MedianFinder:
    def __init__(self):
        self.cnt = 0
        self.left_heap = [float("inf")]
        self.right_heap = [float("inf")]
        heapq.heapify(self.left_heap)
        heapq.heapify(self.right_heap)
        self.median = None

    def addNum(self, num: int) -> None:
        if num <= -self.left_heap[0]:
            if self.cnt % 2 == 0:
                heapq.heappush(self.left_heap, -num)
                self.median = -self.left_heap[0]
            else:
                heapq.heappush(self.left_heap, -num)
                temp = -heapq.heappop(self.left_heap)
                heapq.heappush(self.right_heap, temp)
                self.median = (-self.left_heap[0] + self.right_heap[0]) / 2
        elif num >= self.right_heap[0]:
            if self.cnt % 2 == 0:
                heapq.heappush(self.right_heap, num)
                temp = heapq.heappop(self.right_heap)
                heapq.heappush(self.left_heap, -temp)
                self.median = -self.left_heap[0]
            else:
                heapq.heappush(self.right_heap, num)
                self.median = (-self.left_heap[0] + self.right_heap[0]) / 2
        else:
            if self.cnt % 2 == 0:
                heapq.heappush(self.left_heap, -num)
                self.median = -self.left_heap[0]
            else:
                heapq.heappush(self.right_heap, num)
                self.median = (-self.left_heap[0] + self.right_heap[0]) / 2

        self.cnt += 1

    def findMedian(self) -> float:
        return self.median

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

explain = """
The key idea for finding the median while numbers are added dynamically is to use two heaps.  
One is a max-heap and the other is a min-heap.  

When a new number is added, we update both heaps to maintain the correct balance, 
so that the median can be retrieved efficiently. 
"""