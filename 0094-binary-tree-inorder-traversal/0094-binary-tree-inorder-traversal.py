# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, node , ans):
        if not node:
            return []
        self.inorder(node.left,ans)
        ans.append(node.val)
        self.inorder(node.right,ans)

        return ans
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        return self.inorder(root , [])

        