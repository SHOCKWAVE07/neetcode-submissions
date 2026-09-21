class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mp = dict()

        def helper(i,temp):
            
            if i == len(nums):
                return 1 if temp == target else 0

            if (i,temp) in mp:
                return mp[(i,temp)]


            add = helper(i+1,temp+nums[i])
            sub = helper(i+1,temp-nums[i])

            mp[(i,temp)] = add + sub

            return mp[(i,temp)]

        return helper(0,0)
        