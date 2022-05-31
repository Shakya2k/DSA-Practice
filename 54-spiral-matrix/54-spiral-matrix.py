class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """x = [1,0,-1,0]
        y = [0,1,0,-1]
        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for i in range (n)] for j in range (m)]
        count_direction = 0
        count_val_x = 0
        count_val_y = 0
        output = []
        for i in range (m*n):
            if visited[count_val_x][count_val_y] == 1:
                return output
            
            else:
                output.append(matrix[count_val_x][count_val_y])
                visited[count_val_x][count_val_y] = 1
                #print(visited)
                #count_val_x += x[count_direction]
                #count_val_y += y[count_direction]
                if count_val_x == n-1 and y[count_direction] == 1:
                    #count_val_x -= x[count_direction]
                    count_direction += 1

                elif count_val_y == m-1 and x[count_direction] == 1:
                    #count_val_y -= y[count_direction]
                    count_direction += 1

                elif count_val_x == 0 and y[count_direction] == -1:
                    #count_val_x -= x[count_direction]
                    count_direction += 1

                elif count_val_y == 0 and x[count_direction] == -1:
                    #count_val_y -= y[count_direction]
                    count_direction += 1
                    
                if count_direction > 3:
                    count_direction = 0
                    
                count_val_x += y[count_direction]
                count_val_y += x[count_direction]
                #print (count_val_x, " ", count_val_y)

                if (count_val_y < n and count_val_x < m and count_val_x >= 0 and count_val_y >= 0) and (visited[count_val_x][count_val_y] == 1):
                    count_val_x -= y[count_direction]
                    count_val_y -= x[count_direction]
                    #print (count_val_x, " ", count_val_y)
                    count_direction += 1
                    if count_direction > 3:
                        count_direction = 0
                    count_val_x += y[count_direction]
                    count_val_y += x[count_direction]
                    #print (count_val_x, " ", count_val_y)
                if count_direction > 3:
                    count_direction = 0
                if visited[count_val_x][count_val_y] == 1:
                    return output"""
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left<right and top<bottom:
            #append from left to right
            for i in range(left,right):
                res.append(matrix[top][i])
            top+=1
            #top to bottom
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right-=1
            #edge case: what if we have a row matrix or a col matrix, we ll go out of bounds
            if not (left < right and top<bottom):
                break
            #right to left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom-=1
            #bottom up
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left+=1
        
        return res
                
                
                
                
                
            