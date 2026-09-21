class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_count = 0
        sett = set()
        l = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1
            sett.add(s[r])

            max_count = max(max_count, r-l+1)

        return max_count



        