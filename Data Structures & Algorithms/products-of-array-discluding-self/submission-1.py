class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        right = [1]*len(nums)
        left = [1]*len(nums)
        product = 1
        for i in range(1,len(nums)):
            product*=nums[i-1]
            left[i]=product

        product = 1
        for i in range(len(nums)-2,-1,-1):
            product*=nums[i+1]
            right[i]=product

        for i in range(len(left)):
            left[i]*=right[i]

        return left


        