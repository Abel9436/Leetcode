class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        last_index = len(nums)-1

        for i in range(n-1,-1,-1):
            max_jump = nums[i]
            if i + max_jump >= last_index:
                last_index = i
        return last_index == 0
            


        