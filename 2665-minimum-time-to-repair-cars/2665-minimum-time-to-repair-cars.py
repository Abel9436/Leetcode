class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left , right  = 1 , max(ranks) * (cars ** 2)

        mid  = 0
        ans = 0

        while left < right:
            mid = (left + right ) // 2
            
            total_hrs = sum((int((mid/rank) ** 0.5)) for rank in ranks)
            

            if total_hrs >= cars:
                right = mid
            else:
                left = mid +1
        return left