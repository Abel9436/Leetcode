# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def inorder(self, node , ans):
    #     if not node:
    #         return []
    #     self.inorder(node.left,ans)
    #     ans.append(node.val)
    #     self.inorder(node.right,ans)

    #     return ans


    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            inorder(node.right)
            ans.append(node.val)
        inorder(root)
        return ans
        