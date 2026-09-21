class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        def helper(temp,i):

         
            ans.append(temp.copy())
         

            prev = None
            for j in range(i,len(nums)):
                if prev == nums[j]:
                    continue

                temp.append(nums[j])
                helper(temp,j+1)
                temp.pop()

                prev = nums[j]

            return

        helper([],0)

        return ans

                

            
            
        