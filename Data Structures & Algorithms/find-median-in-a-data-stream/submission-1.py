class MedianFinder:

    def __init__(self):
        self.s = []
        self.l = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.s,-num)

        if self.s and self.l and -self.s[0] > self.l[0]:
            heapq.heappush(self.l,-heapq.heappop(self.s))

        if len(self.s) > len(self.l) + 1:
            heapq.heappush(self.l,-heapq.heappop(self.s))
        if len(self.l) > len(self.s) + 1:
            heapq.heappush(self.s,-heapq.heappop(self.l))        
        

    def findMedian(self) -> float:
        if len(self.s) > len(self.l):
            return -self.s[0]
        if len(self.s) < len(self.l):
            return self.l[0]

        return (-self.s[0]+self.l[0])/2
            
        
        
        
        
        