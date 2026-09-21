class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        t_mp = dict()
        mp = dict()

        for i in t:
            t_mp[i] = t_mp.get(i,0) + 1
            mp[i] = 0    

        t_count = len(t_mp)
        count = 0
        min_length = len(s)+1
        ans = [-1,-1]
        l,r = 0,0

        while r<len(s):
            
            if s[r] in mp:
                mp[s[r]] += 1
            
                if mp[s[r]] == t_mp[s[r]]:
                    count+=1     
            r+=1

            while count == t_count:

                if min_length > (r-l):
                    min_length = r-l
                    ans = [l , r]

                if s[l] in mp:

                    if mp[s[l]] == t_mp[s[l]]:
                        count-=1
                    mp[s[l]] -= 1
                l+=1   
                
                 
        if ans[1] > -1:
            return s[ans[0]:ans[1]]
        else:
            return ""

            


        