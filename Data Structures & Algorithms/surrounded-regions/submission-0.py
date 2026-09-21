class Solution:
    def solve(self, board: List[List[str]]) -> None:

        r = len(board)
        c = len(board[0])

        def helper(i,j):
            
            if i < 0 or i >= r or j < 0 or j >= c or board[i][j] != "O":
                return 

            board[i][j] = 'T'
            helper(i+1,j)  
            helper(i-1,j)  
            helper(i,j-1)  
            helper(i,j+1)

            return

        for i in range(r):
            helper(i,0) 
            helper(i,c-1) 
        
        for j in range(c):
            helper(0,j)
            helper(r-1,j)
            
        for i in range(r):
            for j in range(c):
                if board[i][j] == "T":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        return None