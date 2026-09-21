class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pacific = set()
        atlantic = set()
        r = len(heights)
        c = len(heights[0])
        

        def helper(x,y,prev,visit):
            
            if x < 0 or x >= r or y < 0 or y >= c:
                return

            if (x,y) in visit:
                return
            if heights[x][y] >= prev and (x,y):
                visit.add((x,y))
                prev = heights[x][y]
            
                helper(x+1,y,prev,visit)
                helper(x-1,y,prev,visit)
                helper(x,y+1,prev,visit)
                helper(x,y-1,prev,visit)

            return

        res = []
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    helper(i,j,0,pacific)
                if i==r-1 or j==c-1:
                    helper(i,j,0,atlantic)
        
        for i in range(r):
            for j in range(c):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])       

        return res

        