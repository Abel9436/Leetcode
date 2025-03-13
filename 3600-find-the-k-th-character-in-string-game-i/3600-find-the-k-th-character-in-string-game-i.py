import math

class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Number of steps needed (log2(k) rounded up)
        steps = int(math.ceil(math.log(k, 2)))
        #print(f"Steps: {steps}, k: {k}")
        
        def helper(n, k):
            if n == 0:  # Base case: 0 steps, string is "a"
                return 'a'
            
            prev_len = 2 ** (n - 1)  # Length of previous string
            if k <= prev_len:
                return helper(n - 1, k)
            else:
                # Transform: increment the character at position (k - prev_len) from previous string
                prev_char = helper(n - 1, k - prev_len)
                return chr(ord(prev_char) + 1)
        
        return helper(steps, k)