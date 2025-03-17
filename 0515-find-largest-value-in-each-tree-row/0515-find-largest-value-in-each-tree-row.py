# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []

        def get_max(root,level):
            if not root:
                return

            if level == len(ans):
                ans.append(root.val)
            
            else:
                ans[level]  = max(ans[level],root.val)
            
            get_max(root.left,level + 1)
            get_max(root.right , level +1)
        get_max(root, 0)
        return ans


        