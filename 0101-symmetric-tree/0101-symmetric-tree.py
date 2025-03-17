# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, LeftNode , RightNode):
        if (LeftNode == None or RightNode == None):
            return LeftNode == RightNode
        return (LeftNode.val  == RightNode.val) and self.helper(LeftNode.left,RightNode.right) and self.helper(LeftNode.right, RightNode.left )
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return  self.helper(root.left,root.right)



        