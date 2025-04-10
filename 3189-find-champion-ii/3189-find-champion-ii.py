class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        winner = defaultdict(list)

        for w , l in edges:

            winner[w].append(l)
        
        print(winner)
        def dfs(s_node):
            visited = set()

            def can_reach(node):
                visited.add(node)
                for neigh in winner[node]:

                    if neigh not in visited:
                        can_reach(neigh)
            
            can_reach(s_node)
            return len(visited) == n


        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)
        
        
        return ans[0] if len(ans) == 1 else -1 
