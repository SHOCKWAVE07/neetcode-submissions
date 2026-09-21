class Solution:

    def isAnagram(self, str1:str, str2:str) -> bool:

        mp1 , mp2 = {}, {}

        for i in range(len(str1)):
            mp1[str1[i]] = mp1.get(str1[i],0) + 1
            mp2[str2[i]] = mp2.get(str2[i],0) + 1

        return mp1 == mp2



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []

        index_to_drop = []

        for i in range(len(strs)):
            temp_anagram = []
            if i not in index_to_drop:
                temp_anagram.append(strs[i])
                index_to_drop.append(i)

                for j in range(i+1,len(strs)):

                    if j not in index_to_drop and len(strs[i]) == len(strs[j]):
                        if self.isAnagram(strs[i],strs[j]):
                            temp_anagram.append(strs[j])
                            index_to_drop.append(j)
            if temp_anagram:
                anagrams.append(temp_anagram)

        return anagrams
                    
            
                
                

        