class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        srow=0
        erow=len(matrix)
        scol = 0
        ecol = len(matrix[0])
        while srow<erow:

            mrow = srow + (erow-srow)//2

            if target > matrix[mrow][ecol-1]:
                srow = mrow+1
            else:
                erow = mrow

        if srow == len(matrix):  
            return False

        while scol<ecol:

            mcol = scol + (ecol-scol)//2

            if target == matrix[erow][mcol]:
                return True

            elif target > matrix[erow][mcol]:
                scol = mcol+1
            
            else:
                ecol = mcol

        return False
        