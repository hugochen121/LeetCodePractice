class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        if not matrix or not matrix[0]:
            return False

        nrow, ncol = len(matrix), len(matrix[0])
        curr = matrix[0]
        for i in range(1, nrow):
            if curr[:-1]!=matrix[i][1:]:
                return False

        return True        
