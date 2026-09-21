class Solution:
    def countSubstrings(self, s: str) -> int:
        even = 0 
        odd = 0
        def parser(i,j,count):

            while i>=0 and j<len(s) and s[i]==s[j]:
                count+=1
                i-=1
                j+=1

            return count

        for i in range(len(s)):

            even += parser(i,i,0)

            odd += parser(i,i+1,0)


                
        return even + odd

        