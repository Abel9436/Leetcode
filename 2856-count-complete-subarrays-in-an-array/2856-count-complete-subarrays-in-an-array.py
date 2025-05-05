class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(Counter(nums))
        counter = 0

        for i in range(len(nums)):
            arr = defaultdict(int)
            u = 0
            for j in range(i , len(nums)):
                if arr[nums[j]] == 0:
                    u +=1 
                arr[nums[j]] +=1 

                if u == n:
                    counter +=1
            
        return (counter)







        
