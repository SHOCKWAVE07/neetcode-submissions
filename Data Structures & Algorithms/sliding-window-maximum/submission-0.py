
class Solution:
    import heapq
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        ans = []
        for i in range(k):
            heapq.heappush(h,(-nums[i],i))
        ans.append(-h[0][0])
        for j in range(k,len(nums)):
            heapq.heappush(h,(-nums[j],j))

            while h[0][1] <= j - k:
                heapq.heappop(h)

            ans.append(-h[0][0])
            

        return ans

        
            


            





        