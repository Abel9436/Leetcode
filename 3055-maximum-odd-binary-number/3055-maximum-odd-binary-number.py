class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        one_count = s.count('1')
        zero_count = s.count('0')

        leading_one = 0
   
        if one_count >=2:
            leading_one = one_count -1
            
        
        return '1'* leading_one + '0'*zero_count + '1'

        