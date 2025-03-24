# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left , right = 1, n
        # if n == 
        mid = 0
        while left <= right:
            mid = (left + right) //2

            if isBadVersion(mid):
                right = mid -1
            else:
                left = mid + 1
        return left
         