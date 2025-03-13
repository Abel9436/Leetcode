# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def helper(node):
            if node is None :
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)

            return max(left_depth, right_depth) + 1
        return helper(root)
            


        