class Solution:
    def compute(self, node, counter):
        if not node:
            return 0, 0

        left_s, left_c = self.compute(node.left, counter)
        right_s, right_c = self.compute(node.right, counter) 
        total = left_s + right_s + node.val
        t_c = left_c + right_c + 1

        if (total // t_c) == node.val:
            counter[0] += 1
        return total, t_c
        
    def averageOfSubtree(self, root: TreeNode) -> int:
        counter = [0] 

        self.compute(root, counter)
        
        return counter[0]