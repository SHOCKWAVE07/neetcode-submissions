class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = dict()
        max_count = 0

        for i in nums:
            mp[i] = mp.get(i,0) + 1

        for i in nums:
            if i-1 not in mp:
                count=1
                while (i+count) in mp:
                    count+=1 
                max_count = max(max_count,count)     

        return max_count
        