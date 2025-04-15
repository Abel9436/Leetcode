

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []

        
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
            queue = deque([node])

            while queue:
                level_size = len(queue)
                _list = []

                for _ in range(level_size):
                    node = queue.popleft()  
                    _list.append(node.val)  

                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)

                ans.append(_list)

        bfs(adj, root)  

        return ans
