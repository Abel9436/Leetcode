class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # let us sort first 
        i = 0

        while i < len(nums):
            correct_pos = nums[i] -1
            
            if nums[i] != nums[correct_pos]:
                nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
            else:
                i += 1
        res = []
        i = 0
        while i < len(nums):
            correct_pos = nums[i] -1
            
            if i != correct_pos:
                # nums[i] , nums[correct_pos] = nums[correct_pos] , nums[i]
                res.append(nums[i])
            i +=1
            
        
        print(nums)

        return res

