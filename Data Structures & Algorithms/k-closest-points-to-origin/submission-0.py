class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        
        heap = []

        for x,y in points:
            value = x**2 + y**2
            heap.append([value,x,y])

        heapq.heapify(heap)
        res = []

        while k>0:
            dist,x,y = heapq.heappop(heap)
            res.append([x,y])
            k-=1

        return res

        


        
        