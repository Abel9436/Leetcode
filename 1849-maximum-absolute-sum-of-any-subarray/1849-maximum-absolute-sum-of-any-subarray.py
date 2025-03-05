class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prefix_sum = 0
        max_prefix = 0
        min_prefix = 0
        absolute_prefix = 0

        for num in nums:
            prefix_sum += num

            absolute_prefix = max(absolute_prefix , abs(prefix_sum - min_prefix) , abs(prefix_sum - max_prefix) , abs(prefix_sum))

            min_prefix = min(prefix_sum , min_prefix)
            max_prefix = max (prefix_sum , max_prefix)

        return absolute_prefix



        