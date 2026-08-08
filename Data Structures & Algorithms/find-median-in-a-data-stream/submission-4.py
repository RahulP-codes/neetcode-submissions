class MedianFinder:

    def __init__(self):
        self.count = 0
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        self.count += 1
        if not self.right:
            heapq.heappush(self.right, num)
            return
        
        if num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)
        
    def findMedian(self) -> float:
        while len(self.right) > (self.count+1)//2:
            temp = heapq.heappop(self.right)
            heapq.heappush(self.left, -temp)
        while len(self.left) > self.count//2:
            temp = heapq.heappop(self.left)
            heapq.heappush(self.right, -temp)

        # print(self.left)
        # print(self.right)

        if self.count%2:
            return self.right[0]
        else:
            return (self.right[0] - self.left[0])/2
        