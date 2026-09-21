class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        mp_s, mp_t = {}, {}

        for i in range(len(s)):
            mp_s[s[i]] = mp_s.get(s[i],0) + 1
            mp_t[t[i]] = mp_t.get(t[i],0) + 1

        return mp_s == mp_t

            
        