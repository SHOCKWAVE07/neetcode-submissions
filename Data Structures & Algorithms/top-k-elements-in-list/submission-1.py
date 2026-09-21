class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict()

        for i in nums:
            mp[i] = mp.get(i,0)+1

        buckets = [[] for i in range(len(nums)+1)]

        for i in mp:
            buckets[mp[i]].append(i)
        
        print(buckets)

        ans = []
        for i in buckets[::-1]:
            if k == 0:
                break
            if i:
                for j in i:
                    ans.append(j)
                    k-=1

        return ans