class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        mp = dict()
        
        def helper(i,temp):

            if i == len(coins) or temp>amount:
                return 0

            if (i,temp) in mp:
                return mp[(i,temp)]

            if temp == amount:
                return 1

            temp+=coins[i]
            take=helper(i,temp)
            temp-=coins[i]
            skip=helper(i+1,temp)
            mp[(i,temp)] = take + skip
            return mp[(i,temp)]

        return helper(0,0)

            
            
