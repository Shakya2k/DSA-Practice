class Solution:
    def unpack_matrix(self, matrix: List[List[int]]) -> list:
        m = len(matrix)
        n = len(matrix[0])
        unpacked_matrix = []
        for i in range (m):
            for j in range (n):
                unpacked_matrix.append(matrix[i][j])
        return unpacked_matrix
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        unpacked_matrix = self.unpack_matrix(mat)
        if r*c == len(unpacked_matrix):
            output = [[0 for i in range (c)] for j in range (r)]
            count = 0
            for i in range (r):
                for j in range (c):
                    output[i][j] = unpacked_matrix[count]
                    count += 1
        else:
            output = mat
        return output
        