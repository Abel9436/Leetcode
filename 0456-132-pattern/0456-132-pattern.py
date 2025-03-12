class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        

        stack  = []

        s = float('-inf')
        nums.reverse()

        for num in nums:

            if num < s :
                return True
            
            
            while stack and stack[-1] < num:
                s = stack.pop()
            stack.append(num)
                
        return False
            

        