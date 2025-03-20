# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    def compute(self,node):
        if not node:
            return 
        
        self.compute(node.right)
        self.ans += node.val 
        node.val = self.ans
        self.compute(node.left)


    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.compute(root)
        return root

        
        