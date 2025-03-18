# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sum_nodes(self,node , num):
        if not node:
            return 0
        num = num  * 10 + node.val

        if not node.left and not node.right:
            return num
        else:
            return self.sum_nodes(node.left,num) + self.sum_nodes(node.right,num)
    
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        return self.sum_nodes(root,0)

        