class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [0]*(len(cost)+2)

        def helper(i):
            
            if i > len(cost):
                return float('inf')

            if i == len(cost):
                return 0

            if cache[i]:
                return cache[i]

            cost1 = helper(i+1)
            cost2 = helper(i+2)

            cache[i] = cost[i] + min(cost1,cost2)

            return cache[i]

        return min(helper(0),helper(1))
        