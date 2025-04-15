# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ## DFS
        # value = root.val

        # def dfs(node):
        #     if not node:
        #         return True
            

        #     if value != node.val:
        #         return False

        #     l = dfs(node.left)
        #     r = dfs(node.right)
        #     return l and r

    
        # return dfs(root)

        #BFS

        adj = defaultdict(list)
        def get_adj(node):
            if not node:
                return
            
            if node.left:
                adj[node].append(node.left)
                get_adj(node.left)
            if node.right:
                adj[node].append(node.right)
                get_adj(node.right)

        get_adj(root)
       
        def bfs(graph, node):

            visited = set([node])
            queue= deque([node])
            _list = []

            while queue:
                node = queue.popleft()

                _list.append(node.val)

                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
            
            return _list
        
        
        
        return len(set(bfs(adj,root))) == 1





