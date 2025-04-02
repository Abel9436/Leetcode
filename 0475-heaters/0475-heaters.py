class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()
    
        
       
        
        max_val = float('-inf')

        for i in range(len(houses)):
            closest  = 0
            
            pos = bisect.bisect_left(heaters,houses[i])
            left_dist = float('inf')
            right_dist = float('inf')

            if (pos -1) >=0 :
                left_dist = abs(heaters[pos -1] - houses[i]) 
            if pos < len(heaters):
                right_dist =  abs(heaters[pos] - houses[i]) 
            
            closest = min(left_dist , right_dist)
            max_val = max(max_val , closest)
        
        return max_val
            


            

        
