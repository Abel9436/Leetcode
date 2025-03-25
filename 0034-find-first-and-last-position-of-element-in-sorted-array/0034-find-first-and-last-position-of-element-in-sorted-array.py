class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # first = last = -1
        
        # # Find the first occurrence
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         first = mid
        #         right = mid - 1  
                
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # # Find the last occurrence
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         last = mid
        #         left = mid + 1  

        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return [first, last]

        first =  bisect.bisect_left(nums,target)
        last = bisect.bisect_right(nums,target)

        return [-1,-1] if first == last else [first,last -1]

