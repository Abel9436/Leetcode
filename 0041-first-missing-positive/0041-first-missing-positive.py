class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] > len(nums) or nums[i] <= 0:
                i +=1
                continue
            correct_pos = nums[i] -1
            if nums[i] != nums[correct_pos]:
                nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
            else:
                i += 1
        
        
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        
        return len(nums) + 1
        