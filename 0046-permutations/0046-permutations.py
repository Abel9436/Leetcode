class Solution:
    
    # tracker = []
    def backtrack(self, t,nums,ans):
        if len(t) == len(nums):
            ans.append(t[:])
            return
        
        for num in nums:
            if num not in t:
                t.append(num)
                self.backtrack(t,nums,ans)
                t.pop()
                

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        self.backtrack([],nums,ans)
        return ans

        