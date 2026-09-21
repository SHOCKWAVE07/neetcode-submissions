class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def helper(candidates,ans,curr,temp,target):
            
            if curr == target:
                ans.append(temp.copy())
                return

            if curr > target or len(candidates)==0:
                return

            prev = None
            for i in range(len(candidates)):
                if prev == candidates[i]:
                    continue

                temp.append(candidates[i])
                curr+=candidates[i]
                helper(candidates[i+1:],ans,curr,temp,target)
                temp.pop()
                curr-=candidates[i]

                prev = candidates[i]



            return 

        helper(candidates,ans,0,[],target)


        return ans
        