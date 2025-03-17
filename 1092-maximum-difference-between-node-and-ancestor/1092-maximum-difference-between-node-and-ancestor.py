# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def find_max_diff(self,node,max_,min_):
        if node is None:
            return max_ - min_
        
        max_ = max(max_,node.val)
        min_ = min(min_, node.val)

        left_difference = self.find_max_diff(node.left,max_,min_)
        right_difference = self.find_max_diff(node.right,max_,min_)

        return max(left_difference , right_difference)
    def maxAncestorDiff(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        return self.find_max_diff(root,root.val,root.val)





        