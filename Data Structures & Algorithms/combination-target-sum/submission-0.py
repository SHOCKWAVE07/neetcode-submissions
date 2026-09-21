class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []

        def helper(ans,temp,curr,nums,target):
            
            if curr>target or len(nums)==0:
                return

            if curr == target:
                ans.append(temp.copy())
                return

            temp.append(nums[0])
            curr+=nums[0]

            helper(ans,temp,curr,nums,target)
            temp.pop()
            curr-=nums[0]
            helper(ans,temp,curr,nums[1:],target)

            return 

        helper(ans,[],0,nums,target)

        return ans
        