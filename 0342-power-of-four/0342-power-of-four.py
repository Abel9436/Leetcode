class Solution(object):
    import math
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<= 0:
            return False

        log_val = math.log(n,4)//1

        if 4** log_val == n:
            return True
        return False






        