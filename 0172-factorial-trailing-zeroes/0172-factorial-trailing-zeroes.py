class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # counter = 0
        # while n >= 5:
        #     n //=5
        #     counter +=n
        # return counter



        def trailings(n):
            ans = 0
            if n < 5:
                return ans
            else:
                ans = n // 5
                return ans + trailings(n // 5)

        return trailings(n)

        