class Solution:
     
    def combine(self, n: int, k: int) -> List[List[int]]:
        # self./
        res = []
        candidates = list(range(1,n+1))
        def dfs(start,ans):
            if len(ans) == k:
                res.append(ans.copy())
                return
            if start == len(candidates):
                return
            
            # for i in range(start,n+1):
            ans.append(candidates[start])
            dfs(start +1,ans)
            ans.pop()
            dfs(start +1,ans)

        
                
        dfs(0,[])
        return res

        

        