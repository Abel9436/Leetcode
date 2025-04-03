class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            correct_pos = nums[i] -1
            
            if i != correct_pos and nums[i] != nums[correct_pos]:
                nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
            else:
                i += 1
        ans = []

        for j in range(len(nums)):
            if j+ 1 != nums[j]:
                ans.append(j + 1)
        
        return ans
        

        