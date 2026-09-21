class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for i in range(n)]
        
        ans = []

        cols = set() # c
        negD = set() # r - c
        posD = set() # r + c

        def solver(r): 
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in posD or (r-c) in negD:
                    continue
                
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                board[r][c] = 'Q'

                solver(r+1)

                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
                board[r][c] = '.'  

        solver(0)

        return ans
        