class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        row = []


        for i in range(rowIndex + 1):

            binomial = (math.factorial(rowIndex))//(math.factorial(i) * math.factorial( rowIndex- i))
            row.append(binomial)
        return row
            

        