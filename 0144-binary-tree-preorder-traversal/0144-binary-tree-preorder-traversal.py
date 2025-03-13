class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        
        def preorder(node):
            if node is None:
                return
            ans.append(node.val) 
            preorder(node.left)    
            preorder(node.right) 

        preorder(root) 
        return ans  
