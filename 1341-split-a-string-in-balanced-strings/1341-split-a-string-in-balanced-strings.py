class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0

        ans = 0

        for char in s:

            if char == "L":
                balance += 1
            else:
                balance -=1
            
            if balance == 0:
                ans+=1
        

        return ans




     

        