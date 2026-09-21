class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(i,j,paths):

            if i>=m or j >=n:
                return 0

            if i == m-1 and j == n-1:
                return 1

            paths = helper(i+1,j,paths) + helper(i,j+1,paths)

            return paths

        return helper(0,0,0)
        