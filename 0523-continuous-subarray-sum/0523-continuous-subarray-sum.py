class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        prefix_ = 0
        remainder = defaultdict(int)

        remainder[0] =-1
        rem =0

        for i,num in enumerate(nums):

            prefix_ += num
            rem = prefix_ if k == 0 else prefix_ %  k

            if rem not in remainder:
                remainder[rem] = i
            else:
                if i - remainder[rem] > 1:
                    return True
        return False

        




        