import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for i in stones:
            heapq.heappush(heap,-i)

        while len(heap)>1:
            num1 = heapq.heappop(heap)
            num2 = heapq.heappop(heap)

            heapq.heappush(heap,-abs(num1-num2))

        return -heap[0]



        