class MedianFinder:
    def __init__(self):
        self.data = []

    def addNum(self, num: int):
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        return (self.data[n // 2] if (n & 1) else
                (self.data[n // 2] + self.data[n // 2 - 1]) / 2)