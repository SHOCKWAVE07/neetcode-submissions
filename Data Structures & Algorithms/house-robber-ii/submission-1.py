class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return nums[0]

        def rob_linear(nums):
            m = len(nums)
            cache = [-1] * m

            def helper(i):
                if i >= m:
                    return 0
                if cache[i] != -1:
                    return cache[i]
                # either skip current house OR rob it
                cache[i] = max(helper(i+1), nums[i] + helper(i+2))
                return cache[i]

            return helper(0)

        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
        