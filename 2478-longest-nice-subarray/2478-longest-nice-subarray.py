from collections import deque

class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        current_mask = 0  # Mask to store the OR of all numbers in the current window
        left = 0  # Left pointer of the sliding window
        
        for right in range(len(nums)):
            # If the current number overlaps (i.e., the & is non-zero), move the left pointer
            while (current_mask & nums[right]) != 0:
                current_mask ^= nums[left]  # Remove the effect of the leftmost element
                left += 1
            
            current_mask |= nums[right]  # Add the current number to the mask
            max_len = max(max_len, right - left + 1)  # Update max_len

        return max_len
