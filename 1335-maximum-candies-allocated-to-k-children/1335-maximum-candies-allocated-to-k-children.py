class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
       
        left , right = 1 , max(candies) 
        ans = 0

        while left <= right:
            mid  = (left + right) // 2
            
            healper = sum((candy // mid) for candy in candies)
            if healper >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
                

        # return min(candies)
        

        