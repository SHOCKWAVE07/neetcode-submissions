class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [0]*(n+1)
        
        def helper(i):
            if i > n:
                return 0
                
            if cache[i]:
                return cache[i]
            
            if i == n:
                return 1
            cache[i] = helper(i+1) + helper(i+2)
            return cache[i]
        

        return helper(0)

        