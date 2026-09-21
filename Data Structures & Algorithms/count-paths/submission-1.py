class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = [[0]*n for _ in range(m)]
  
        def helper(i,j):

            if i>=m or j >=n:
                return 0

            if i == m-1 and j == n-1:
                return 1

            if cache[i][j]:
                return cache[i][j]

            cache[i][j] = helper(i+1,j) + helper(i,j+1)

            return cache[i][j]

        return helper(0,0)
        