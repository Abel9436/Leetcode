class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0, x -1

        if x == 0 or x == 1:
            return x
        ans = 0
        mid = 0

        while right >= left:
            mid = (left + right) // 2
            if (mid*mid) == x:
                return mid
            if (mid * mid ) <  x:
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        return ans
        