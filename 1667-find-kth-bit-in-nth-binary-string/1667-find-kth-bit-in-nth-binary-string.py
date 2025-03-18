class Solution(object):
    def find(self, n , k):
        if n == 1:
            return '0'

        length = 2 ** n -1
        mid = length //2 + 1

        if k == mid:
            return '1'
        if k < mid:
            return self.find(n-1,k)
        if self.find(n-1, 1+ length -k) == '0':
            return '1'

        else:
            return '0'


    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return self.find(n,k)


        




        