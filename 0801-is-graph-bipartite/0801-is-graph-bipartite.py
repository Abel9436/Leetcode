class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        a_graph = defaultdict(int)
        for i in range(n):
            a_graph[i] = graph[i]
            # graph[v].append(u)


        colors = {}

        for source in a_graph:
            if source not in colors:
                queue=deque([(source  , 0)])
                colors[source] = 0
            
            while queue:
                u , color_red = queue.popleft()

                for v in a_graph.get( u , []):
                    if v not in colors:

                        queue.append((v , 1 - color_red ))
                        colors[v] = 1 - color_red
                    elif colors[v] == color_red:
                        return False
        return True


