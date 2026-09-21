from collections import defaultdict



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares, rows, cols = defaultdict(list), defaultdict(list), defaultdict(list)

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                sq_index = (i//3, j//3) 
                if num != '.':
                    if num in rows[i]:
                        return False
                    else:
                        rows[i].append(num)

                    if num in cols[j]:
                        return False
                    else:
                        cols[j].append(num)

                    if num in squares[sq_index]:
                        return False
                    else:
                        squares[sq_index].append(num)

                
        return True



                    
