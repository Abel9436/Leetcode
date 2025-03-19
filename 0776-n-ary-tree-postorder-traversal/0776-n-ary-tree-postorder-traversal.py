"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self,root,ans):
        
        if not root:
            return 

        for child in root.children:
            self.dfs(child,ans)
        ans.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        self.dfs(root,ans)

        return ans
        
       