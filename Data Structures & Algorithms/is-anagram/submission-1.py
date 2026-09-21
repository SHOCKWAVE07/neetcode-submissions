class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mp = dict()

        for i in s:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1

        for j in t:
            if j in mp and mp[j]>0:
                mp[j]-=1
            else:
                return False

        for k,v in mp.items():
            if mp[k] != 0:
                return False

        return True

            
        