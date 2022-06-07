class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = [[0]*n for _ in range (n)]
        
        row, col, i, way = 0, 0, 1, 0
        
        while i <= n*n:
            ans[row][col] = i
            
            if (row + direction[way][0] >= n or col + direction[way][1] >= n or ans[row+direction[way][0]][col+direction[way][1]] != 0):
                if way == 3:
                    way = 0
                else:
                    way += 1
            row += direction[way][0]
            col += direction[way][1]
            i += 1
            
        return ans