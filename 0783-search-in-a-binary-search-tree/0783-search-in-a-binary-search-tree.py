# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def search(self,root,val):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.search(root.left,val)
        return self.search(root.right,val)
    def searchBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        # ans = []
        # if root is None:
        #     return None
        
        # # if root.val < 
        def search(node):
            if node is None:
                return None


            
            if node.val == val:
                return node
            # preorder(node)

            if node.val > val:
                search(node.left)
            if node.val < val:
                search(node.right)
        # search(root)

        return self.search(root,val)






























        