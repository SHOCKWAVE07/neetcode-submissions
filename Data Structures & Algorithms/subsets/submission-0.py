class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def helper(nums,ans,temp):

            if len(nums) == 0:
                ans.append(temp.copy())
                return

            temp.append(nums[0])
            helper(nums[1:],ans,temp)
            temp.pop()
            helper(nums[1:],ans,temp)

            return 0
        helper(nums,ans,[])
        return ans