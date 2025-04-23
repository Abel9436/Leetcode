class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        # graph = defaultdict(list)
        # indegree = [0 for _ in range(numCourses)]
        # queue = deque()
        # order = []
        

        # for c, p in prerequisites:

        #     graph[p].append(c)

        #     indegree[c] += 1
        
        # for d in range(numCourses):
        #     if indegree[d] == 0:
        #         queue.append(d)
        
        # while queue:
        #     node = queue.popleft()

        #     for nei in graph[node]:
        #         indegree[nei] -=1
        #         if indegree[nei] == 0:
        #             queue.append(nei)
        #     order.append(node)
        # if len(order) != numCourses:
        #     return []
        
        # return order



        ############

        #let us solve it by dfs

        graph = defaultdict(list)

        for c, p in prerequisites:

            graph[p].append(c)
         
        visited = [0] * numCourses

        stack = []

        def dfs(node):

            visited[node] = 1

            for nei in graph.get(node , []):
                if visited[nei] == 1:
                    return True
                if visited[nei] == 0:
                    if dfs(nei):
                        return True
            visited[node] = 2
            stack.append(node)
            return False
        
        for node in range(numCourses):
            if visited[node] == 0:
                if dfs(node):
                    return []

        return stack[::-1]

