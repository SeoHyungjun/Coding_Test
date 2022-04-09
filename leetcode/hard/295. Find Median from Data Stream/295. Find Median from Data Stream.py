class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.cnt = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
        self.cnt += 1

    def findMedian(self) -> float:
        if self.cnt % 2 != 0:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


'''
그냥 로직에 따라 구현

class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        length = len(self.arr)
        
        if length % 2 == 0:
            return (self.arr[length//2 - 1] + self.arr[length//2]) / 2
        
        else:
            return self.arr[length//2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''