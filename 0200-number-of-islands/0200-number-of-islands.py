class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited =[ [ False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        count = 0
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))


        def dfs(row , col):
            if not inbound(row , col) or  visited[row][col] or grid[row][col] == "0":
                return
            visited[row][col] = True
            dfs(row +1 ,col)
            dfs(row -1 ,col)

            dfs(row ,col +1)

            dfs(row ,col -1)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count