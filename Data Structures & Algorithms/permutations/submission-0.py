class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        mp = dict()

        for i in nums:
            mp[i] = False

        def helper(mp,temp,ans):

            if len(temp)==len(mp):
                ans.append(temp.copy())
                return

            for i in mp:
                if mp[i] == False:
                    temp.append(i)
                    mp[i] = True
                    helper(mp,temp,ans)
                    mp[i] = False
                    temp.pop()
            return 

        helper(mp,[],ans)

        return ans
            
            
        