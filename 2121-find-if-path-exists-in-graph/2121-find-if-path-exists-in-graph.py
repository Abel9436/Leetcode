class Solution:
    def dfs(self , graph , node , visited , destination):

        if node == destination:
            return True
        

        visited.add(node)
        for neigh in graph[node]:

            if neigh not in visited:
                found = self.dfs(graph , neigh , visited , destination)
            
                if found:
                    return True
        return False




    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph  = defaultdict(list)

        for node1 , node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # print(graph)
        visited = set()

        return self.dfs(graph ,source, visited , destination)