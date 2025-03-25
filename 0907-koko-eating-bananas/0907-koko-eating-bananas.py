class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        left , right  = 1 , max(piles)

        mid  = 0

        while left < right:
            mid = (left + right ) // 2
            if mid != 0:
                total_hrs = sum(math.ceil(pile/mid) for pile in piles)
            else:
                total_hrs = sum(math.ceil(pile) for pile in piles)

            if total_hrs <= h:
                right = mid
            else:
                left = mid +1
        return left