class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        counter = 0

        for i in range(n-2):
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i+1] = 1 - nums[i + 1]
                nums[i+2] = 1 - nums[i + 2]
                counter += 1

        print(counter)
        if any(num == 0 for num in nums[-3:]):
            return -1
        
        return counter
