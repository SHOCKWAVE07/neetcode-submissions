class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        mp = {}

        def dfs(i, j, t):
            # Out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            # Empty cell
            if grid[i][j] == 0:
                return

            # If this cell is visited with a smaller/equal time, stop
            if (i, j) in mp and mp[(i, j)] <= t:
                return

            # Record infection time
            mp[(i, j)] = t

            # Spread to neighbors
            dfs(i + 1, j, t + 1)
            dfs(i - 1, j, t + 1)
            dfs(i, j + 1, t + 1)
            dfs(i, j - 1, t + 1)

        # Run DFS from all rotten oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    dfs(i, j, 0)

        # Check if any fresh orange is left
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in mp:
                    return -1

        # Find max infection time
        return max(mp.values(), default=0)
