class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high:
            mid = low + (high - low) // 2
            day = 1
            store = 0

            for i in range(len(weights)):
                if store + weights[i] <= mid:
                    store += weights[i]
                else:
                    store = weights[i]
                    day += 1

            if day <= days:
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        
        return ans
        
                