class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == [[0]] or grid == [[0,0,0,0]]:
            return 0
        
        row , col = len(grid) , len(grid[0])


        empty , fresh , rotten = 0 , 1 , 2


        no_of_fresh = 0
        

        queue = deque()
        DIR = [[0,1],[1,0], [0,-1], [-1,0]]
        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col



        for i in range(row):
            for j in range(col):

                if grid[i][j] == rotten:
                    queue.append((i,j))
        ans = 0
        while queue:
            for _ in range(len(queue)):
                i , j = queue.popleft()

                for di , dj in DIR:
                    new_i = i + di
                    new_j = j + dj
                    if inbound(new_i , new_j) and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2
                        queue.append((new_i, new_j))
                        # noo_
            ans +=1

        for i in range(row):
            for j in range(col):

                if grid[i][j] == fresh:
                    return -1

        return ans - 1

                



