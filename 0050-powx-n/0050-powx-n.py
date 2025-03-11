class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # return x ** n
        def power(x,n):
            if n == 0 :
                return 1
            
            if n < 0:
                return 1 / power(x,-n)
            
            if n % 2  == 0:
                half = power(x,n // 2)
                return half * half
            else:
                return x * power(x,n-1)

        return power(x,n)

        