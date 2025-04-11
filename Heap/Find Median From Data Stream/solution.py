import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # Push value to small heap
        heapq.heappush(self.small, -1 * num)

        # Check to see if all nums in small are <= all nums in large
        if (self.small and self.large and (self.small[0] * -1) > self.large[0]):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        # Check to see that the lengths of heaps are similar (within 1 of the other)
        if len(self.small) - len(self.large) > 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) - len(self.small) > 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()