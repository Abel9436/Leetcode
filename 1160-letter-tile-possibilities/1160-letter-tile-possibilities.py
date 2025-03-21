class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        #let me use backtracking template
        # ans  = set()
        # tracker = set()
        # def backtrack(index):
        #     if index == len(tiles):
            
        #         for p in tracker:
                    
        #             ans.add(p)
        #             ans.add(p[::-1])
        #         return
            
        #     backtrack(index + 1)
        #     tracker.add(tiles[index])
        #     backtrack( index +1)
        #     if tracker:
        #         tracker.pop()
        # backtrack(0)
        
        # return len(ans)

        def dfs(tile_c):
            comb_c = 0
            for i , v in tile_c.items():
                if v > 0:
                    comb_c +=1
                    tile_c[i] -=1

                    comb_c += dfs(tile_c)

                    tile_c[i] +=1
            return comb_c
        tile_c = Counter(tiles)
        return dfs(tile_c)
            
