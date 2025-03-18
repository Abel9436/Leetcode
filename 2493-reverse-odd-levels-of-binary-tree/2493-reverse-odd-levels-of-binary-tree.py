# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverse_level(self, node):
        if not node:
            return
        node.left , node.right = node.right, node.left

        self.reverse_level(node.left)
        self.reverse_level(node.right)

            
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        # def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        
        queue = deque([root])
        level = 0  
        
        while queue:
            level_size = len(queue)
            current_level_list = []
            for _ in range(level_size):
                nod = queue.popleft()

                if level % 2 != 0:
                    current_level_list.append(nod)

                if nod.left:
                    queue.append(nod.left)
                if nod.right:
                    queue.append(nod.right)
                
            if current_level_list:
                left , right = 0 , len(current_level_list) -1

                while left < right:
                    current_level_list[left].val , current_level_list[right].val = current_level_list[right].val , current_level_list[left].val
                    left +=1
                    right -=1
            level +=1

                
        return root

