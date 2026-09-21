class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        mp = {}

        def helper(i,j,t):

            if i<0 or i>=len(grid) or j < 0 or j >= len(grid[0]):
                return

            if grid[i][j] == 0:
                return

            if (i,j) in mp and mp[(i,j)] <= t:
                return

            mp[(i,j)] = t
            helper(i+1,j,t+1)
            helper(i-1,j,t+1)
            helper(i,j+1,t+1)
            helper(i,j-1,t+1)

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    helper(i,j,0)
           

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in mp:
                    return -1      

        return max(mp.values(), default=0)
        
        