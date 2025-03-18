# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def get_zigzag(self , node):
        if not node:
            return []

        res = []

        my_que = deque([node])

        level = 0

        while my_que:
            level_list = []

            for _ in range(len(my_que)):
               
                nod = my_que.popleft()
                level_list.append(nod.val)

                if nod.left:
                    my_que.append(nod.left)
                if nod.right:
                    my_que.append(nod.right)
                
            if level % 2 ==0:

                res.append(level_list)

            else:
                res.append(level_list[::-1])

            level+=1

        return res
    
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        return self.get_zigzag(root)
        
        