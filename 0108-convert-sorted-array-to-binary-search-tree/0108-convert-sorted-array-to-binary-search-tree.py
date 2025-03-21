# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2

        node =  TreeNode(nums[mid])
        node.left = self.dfs(nums[:mid])
        node.right = self.dfs(nums[mid+1:])

        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.dfs(nums)




        