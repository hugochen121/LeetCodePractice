class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 25%
        '''
        if not(grid) or not(grid[0]): return 0

        rowN , colN = len(grid), len(grid[0])

        def helper(x, y, grid):
            if x<0 or y<0 or x>=rowN or y>=colN or grid[x][y]=="0":
                return 0
            dist = 1
            grid[x][y] = "0"
            dist+=helper(x+1, y, grid)  # int +string -> time-consuming
            dist+=helper(x, y+1, grid)
            dist+=helper(x-1, y, grid)
            dist+=helper(x, y-1, grid)
            return dist

        counter = 0
        for i in range(rowN):
            for j in range(colN):
                result = helper(i, j, grid)
                if result: counter+=1
        return counter
        

        # 35%
        if not(grid) or not(grid[0]): return 0

        rowN , colN = len(grid), len(grid[0])

        def helper(x, y, grid):
            if x<0 or y<0 or x>=rowN or y>=colN or grid[x][y]=="0":
                return 

            grid[x][y] = "0"
            helper(x+1, y, grid)  # int +string -> time-consuming
            helper(x, y+1, grid)
            helper(x-1, y, grid)
            helper(x, y-1, grid)

        counter = 0
        for i in range(rowN):
            for j in range(colN):
                if grid[i][j]=="1": counter+=1
                helper(i, j, grid)
        return counter
'''

        # 45%
        if not(grid) or not(grid[0]): return 0

        rowN , colN = len(grid), len(grid[0])

        def helper(x, y, grid):
            if x<0 or y<0 or x>=rowN or y>=colN or grid[x][y]=="0":
                return 

            grid[x][y] = "0"
            helper(x+1, y, grid)  # int +string -> time-consuming
            helper(x, y+1, grid)
            helper(x-1, y, grid)
            helper(x, y-1, grid)

        counter = 0
        for i in range(rowN):
            for j in range(colN):
                if grid[i][j]=="1": #onlu check islands
                    counter+=1
                    helper(i, j, grid)
        return counter

