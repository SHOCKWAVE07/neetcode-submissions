class Solution:
    def trap(self, height: List[int]) -> int:
        suffix, prefix = [0]* len(height), [0]*len(height)

        max_s = 0
        for i in range(len(height)):
            suffix[i] = max_s
            max_s = max(max_s,height[i])

        max_p = 0
        for i in range(len(height)-1,-1,-1):
            prefix[i] = max_p
            max_p = max(max_p,height[i])

        water = 0

        for i in range(len(height)):
            trap = min(prefix[i],suffix[i]) - height[i]
            if trap > 0:
                water += trap   

        return water