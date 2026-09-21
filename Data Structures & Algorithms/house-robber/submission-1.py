class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = [0]* (len(nums)+1)

        def helper(i):
            
            if i >= len(nums):
                return 0

            if cache[i]:
                return cache[i]

            cache[i] = nums[i] + max(helper(i+2),helper(i+3))

            return cache[i]

            

        return max(helper(0),helper(1))
        