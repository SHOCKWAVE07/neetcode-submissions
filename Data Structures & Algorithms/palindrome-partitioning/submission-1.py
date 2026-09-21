class Solution:
    def palindrome(self,s,i,j):

        while i < j:

            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return False

        return True    


    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []

        def substrings(i):
            if i >= len(s):
                ans.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.palindrome(s,i,j):
                    part.append(s[i:j+1])
                    substrings(j+1)
                    part.pop()
  
        substrings(0)
    
        return ans


        