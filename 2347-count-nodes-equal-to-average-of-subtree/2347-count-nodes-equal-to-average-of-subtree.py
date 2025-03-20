# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    counter = 0
    def compute(self,node):
        if not node:
            return (0,0)

        left_s , left_c = self.compute(node.left)
        right_s , right_c = self.compute(node.left)

        total = left_s + right_s


        if (total //(left_c + right_c + 1 )) == node.val:
            self.counter +=1
        return total ,left_c + right_c + 1
        
        
    def averageOfSubtree(self, root: TreeNode) -> int:
        # counter = 0
        self.compute(root)
        return self.counter + 1