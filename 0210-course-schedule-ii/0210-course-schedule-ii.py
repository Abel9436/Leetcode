class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        queue = deque()
        order = []
        

        for c, p in prerequisites:

            graph[p].append(c)

            indegree[c] += 1
        
        for d in range(numCourses):
            if indegree[d] == 0:
                queue.append(d)
        
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    queue.append(nei)
            order.append(node)
        if len(order) != numCourses:
            return []
        
        return order
