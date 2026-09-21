class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        ans = []
        area = [0]
        max_area = 0

        def search(r,c):

            if r<0 or r>= len(grid) or c<0 or c>= len(grid[0]) or grid[r][c] == 0:
                return False

            grid[r][c] = 0
            area[0]+=1
            out = search(r+1,c) or search(r,c+1) or search(r-1,c) or search(r,c-1)

            if not out:
                return False

            return True

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    area[0]=0
                    search(i,j)
                    max_area = max(max_area,area[0])
        return max_area
        