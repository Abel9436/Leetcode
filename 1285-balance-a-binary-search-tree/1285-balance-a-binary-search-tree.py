# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make_balanced(self,nums):

        if not nums:
            return None
        mid = len(nums) // 2

        node = TreeNode(nums[mid])

        node.left = self.make_balanced(nums[:mid])
        node.right = self.make_balanced(nums[mid + 1 :])
        
        return node

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # first let me find the inorder
        nums = []

        def inorder(node):
            if not node:
                return 

            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)
       

        return self.make_balanced(nums)
        


