class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1), (0,-1), (1,0) ,(-1,0)]

        premeter = 0
        def is_inbound(row , col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs( row , col):
            nonlocal premeter
            if not is_inbound(row,col) or grid[row][col] == 0:
                premeter +=1
                return 
            if grid[row][col] == 2:
                return
            grid[row][col] = 2

            for row_c , col_c in directions:
                new_row = row + row_c
                new_col = col + col_c
                dfs(new_row , new_col)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return premeter
        return premeter