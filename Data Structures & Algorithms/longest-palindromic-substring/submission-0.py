class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxl = 0

        def explore(i,j):

            while i >= 0 and j < len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return s[i+1:j]


        for i in range(len(s)):

            odd = explore(i,i)

            even = explore(i,i+1)

            if len(odd) > maxl:
                maxl = len(odd)
                res = odd

            if len(even) > maxl:
                maxl = len(even)
                res = even

        return res

        