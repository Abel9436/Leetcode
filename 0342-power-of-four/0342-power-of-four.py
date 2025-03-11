class Solution(object):
    import math
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n<= 0:
        #     return False

        # log_val = math.log(n,4)//1

        # if 4** log_val == n:
        #     return True
        # return False

        def poweroffour(n):

            if n == 1:
                return True
            if n <= 0 or n % 4 != 0:
                return False
            return poweroffour(n//4)

        return poweroffour(n)







        