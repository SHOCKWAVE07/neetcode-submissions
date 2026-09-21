class Solution:

    def helper(self,text1,text2,i,j,mp):

        if i == len(text1) or j == len(text2):
            return 0
        if (i,j) in mp:
            return mp[(i,j)]

        if text1[i] == text2[j]:
            mp[(i,j)]= 1 + self.helper(text1,text2,i+1,j+1,mp)
        else:
            mp[(i,j)] = max(self.helper(text1,text2,i,j+1,mp),self.helper(text1,text2,i+1,j,mp))
            
        return mp[(i,j)]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i , j = 0,0
        mp = {} 
        return self.helper(text1,text2,i,j,mp)

        