# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insert(self,root , val):
        if root is None:
            return ListNode(val)
        

    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def insert(root,val):
            if root is None:
                return TreeNode(val)
            if root.val == val:
                    return root
            if root.val < val:
                root.right = insert(root.right, val)
            else:
                root.left = insert(root.left, val)
            return root
        return insert(root,val)
        
        