class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        answer = []
        for i in range (len(grid[0])):
            col = i
            for row in range (len(grid)):
                if grid[row][col] == 1:
                    if col == len(grid[0]) - 1:
                        answer.append(-1)
                        break
                    if grid[row][col+1] == -1:
                        answer.append(-1)
                        break
                    else:
                        col += 1
                elif grid[row][col] == -1:
                    if col == 0:
                        answer.append(-1)
                        break
                    if grid[row][col-1] == 1:
                        answer.append(-1)
                        break
                    else:
                        col -= 1
                if row == len(grid) - 1:
                    answer.append(col)
        
        return answer
                        
            
        