import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ks = 1
        ke = max(piles)


        while ks < ke:
            kmid = ks + (ke - ks)//2

            hours = sum([math.ceil(i/kmid) for i in piles])

            if hours<=h:
                ke = kmid
            else:
                ks = kmid+1

        return ks


        