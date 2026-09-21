class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq = 0
        l = 0
        mp = dict()


        for r in range(len(s)):
            mp[s[r]] = mp.get(s[r],0)+1

            max_freq = max(max_freq,mp[s[r]])

            if (r - l + 1) - max_freq > k:
                mp[s[l]]-=1
                l+=1
        
        return r-l+1



        