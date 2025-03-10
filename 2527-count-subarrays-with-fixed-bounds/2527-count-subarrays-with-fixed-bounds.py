class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        res = 0
        last_bad = -1 
        last_min = -1
        last_max = -1 
        
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                last_bad = i
                last_min = -1
                last_max = -1
            else:
                if nums[i] == minK:
                    last_min = i
                if nums[i] == maxK:
                    last_max = i
                if last_min != -1 and last_max != -1:
                    res += min(last_min, last_max) - last_bad
        return res