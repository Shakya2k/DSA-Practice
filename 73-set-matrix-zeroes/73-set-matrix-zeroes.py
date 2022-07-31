class Solution(object):
    def con_rows_cols(self, r, c, matrix):
        for i in range (len(matrix[0])):
            matrix[r][i] = 0
        for i in range (len(matrix)):
            matrix[i][c] = 0
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        check = []
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j] == 0:
                    check.append([i,j])
        for i,j in check:
            self.con_rows_cols(i,j,matrix)
                
        