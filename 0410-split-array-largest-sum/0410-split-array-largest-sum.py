class Solution:
    def is_valid(self, mid,nums,k):
        count = 1
        c_sum = 0

        for num in nums:
            if c_sum + num > mid:
                count +=1
                c_sum = num
            else:
                c_sum += num
    
        return count <= k
    def splitArray(self, nums: List[int], k: int) -> int:
        
        left , right  = max(nums) , sum(nums)

        while left < right:

            mid = ( left + right ) // 2

            if self.is_valid(mid,nums,k):
                right = mid 
            else:
                left = mid + 1
        return left