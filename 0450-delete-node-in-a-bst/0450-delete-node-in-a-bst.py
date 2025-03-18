# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_successor(self, node):
        node = node.right
        while node.left is not None:
            node = node.left
        return node

    def delete(self, node, val):
        if node is None:
            return node
        if node.val > val:
            node.left = self.delete(node.left, val)
        elif node.val < val:
            node.right = self.delete(node.right, val)
        else:
            if node.right is None:
                return node.left
            if node.left is None:
                return node.right
            succ = self.get_successor(node)
            node.val = succ.val
            node.right = self.delete(node.right, succ.val)
        return node

    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        return self.delete(root, key)