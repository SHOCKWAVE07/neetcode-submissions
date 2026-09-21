class MedianFinder:

    def __init__(self):
        self.store = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.store,num)
        

    def findMedian(self) -> float:
        temp = []

        n = len(self.store)

        for i in range(n):
            temp.append(heapq.heappop(self.store))

        self.store.extend(temp)
        heapq.heapify(self.store)

        if n %2 ==0:
            return (temp[n//2] + temp[n//2-1])/2
        else:
            return temp[n//2]
        
        
        
        