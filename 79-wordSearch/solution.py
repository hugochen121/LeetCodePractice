class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not(board): return False

        nRow, nCol = len(board), len(board[0])   
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # 12%   origin verison
        # 22%   use "list" for looping, use "set" for random access
        # 32%   pass index but sub-string
        visit = [[False]*nCol for _ in range(nRow)]  

        def helper(x, y, ind):
            if not(word[ind:]):
                return True
            
            if x<0 or x>nRow-1 or y<0 or y>nCol-1 or visit[x][y] or board[x][y]!=word[ind]:
                return False
            
            # print(x, y, remain)
            
            visit[x][y]=True

            for dr, dc in directions:
                if helper(x+dr, y+dc, ind+1):
                    return True

            # remove visit tag after navigation (back-tracking)
            visit[x][y]=False
            return False


        for i in range(nRow):
            for j in range(nCol):
                if helper(i, j, word):
                    return True
                
        return False         