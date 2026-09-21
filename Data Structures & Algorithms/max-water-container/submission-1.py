class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        i = 0
        j = len(heights)-1

        while i<j:
            max_water = max(min(heights[i],heights[j])*(j-i),max_water)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1

        return max_water

        
        