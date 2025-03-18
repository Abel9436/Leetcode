# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,node,p,q):
        if not node:
            return None
            # return node
        if q.val > node.val and p.val > node.val:
            return self.dfs(node.right,p,q)
        elif q.val < node.val and p.val < node.val:
            return self.dfs(node.left,p,q)
        else:
            return node
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root,p,q) 
        
        