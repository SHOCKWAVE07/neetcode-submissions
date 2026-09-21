class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        mp = dict()
        k = len(s1)

        for i in s1:
            mp[i] = mp.get(i,0)+1

        l = 0
        temp_mp = dict()
        for r in range(len(s2)):

            temp_mp[s2[r]] = temp_mp.get(s2[r],0) + 1

            if r - l + 1 > k:
                temp_mp[s2[l]]-=1
                if temp_mp[s2[l]]==0:
                    del temp_mp[s2[l]]

                l+=1

            if r-l+1 == k and mp == temp_mp:
                return True

        return False

            
                




                
        