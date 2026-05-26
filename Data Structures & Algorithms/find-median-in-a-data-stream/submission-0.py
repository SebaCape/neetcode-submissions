class MedianFinder:

    def __init__(self):
        self.min, self.max = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min, -num)

        if self.min and self.max and -self.min[0] > self.max[0]:
            heapq.heappush(self.max, -heapq.heappop(self.min))

        if len(self.min) > len(self.max) + 1:
            heapq.heappush(self.max, -heapq.heappop(self.min))
        elif len(self.max) > len(self.min) + 1:
            heapq.heappush(self.min, -heapq.heappop(self.max))

    def findMedian(self) -> float:
        if len(self.min) > len(self.max):
            return -self.min[0]
        elif len(self.max) > len(self.min):
            return self.max[0]
        return (self.max[0] - self.min[0]) / 2
        