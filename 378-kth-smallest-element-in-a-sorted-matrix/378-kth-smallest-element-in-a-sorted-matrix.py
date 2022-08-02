class Solution(object):
    def con_mat_list(self, matrix):
        l = []
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                l.append(matrix[i][j])
        return l
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        store = self.con_mat_list(matrix)
        store.sort()
        return store[k-1]