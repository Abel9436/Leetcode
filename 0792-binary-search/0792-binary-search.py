class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) -1

        mid  =  0 
        while left <= right:
            mid = (left + right) // 2

            if nums [mid] == target:
                return mid

            if nums[mid] > target:
                right = mid -1
            else:
                left = mid + 1
        return -1 