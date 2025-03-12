class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(n):
            if n == 1:
                return True
            if n <= 0:
                return False
            if n % 2 != 0:
                return False
            return helper(n//2)
        return helper(n)
        