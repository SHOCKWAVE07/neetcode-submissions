class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = []
        product=1

        for i in range(len(nums)):
            for j in range(len(nums)):
                if j==i:
                    continue
                else:
                    product*=nums[j]
            ans.append(product)
            product=1

        return ans
        