class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        # 55%
        if not(board): return
        
        visit= set()
        rowN, colN = len(board), len(board[0])

        def helper(x, y, pattern):
            
            if x<0 or x>rowN-1 or y<0 or y>colN-1: 
                return
            if (x, y) in visit: 
                return
            if pattern != board[x][y]:
                return
            
            visit.add((x, y))

            helper(x-1, y, pattern)    
            helper(x+1, y, pattern)    
            helper(x, y-1, pattern)    
            helper(x, y+1, pattern)    

        
        for i in range(rowN):
            for j in range(colN):
                if i==0 or i==rowN-1 or j==0 or j==colN-1:
                    helper(i, j, board[i][j])

        for i in range(1, rowN):
            for j in range(1, colN):
                if not((i, j) in visit):
                    board[i][j]="X"
                    
