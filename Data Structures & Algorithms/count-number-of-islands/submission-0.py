class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        r = len(grid)
        c = len(grid[0])
        ans = 0

        def search(r,c):

            if r<0 or r>= len(grid) or c<0 or c>= len(grid[0]) or grid[r][c] == '0':
                return False

            grid[r][c] = '0'
            out = search(r+1,c) or search(r,c+1) or search(r-1,c) or search(r,c-1)

            if not out:
                return False

            return True

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    ans+=1
                    search(i,j)

        return ans