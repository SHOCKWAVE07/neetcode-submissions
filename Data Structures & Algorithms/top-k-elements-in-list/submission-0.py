class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict()

        for i in nums:
            mp[i] = mp.get(i,0)+1

        sorted_dict = dict(sorted(mp.items(), key = lambda item : item[1], reverse=True))
        ans = []
    
        for i,j in sorted_dict.items():
            if k == 0:
                break
            ans.append(i)
            k-=1

        return ans