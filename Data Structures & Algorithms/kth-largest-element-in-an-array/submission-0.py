class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapq.heapify(nums)

        for i in range(len(nums)-k+1):
            temp = heapq.heappop(nums)

        return temp
        