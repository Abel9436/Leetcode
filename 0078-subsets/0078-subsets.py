class Solution:


    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        tracker = []
        ans = []
        def backtrack(index):

            if index == n:
                ans.append(tracker[:])
                return
            
            backtrack(index+1)
            tracker.append(nums[index])
            backtrack(index + 1)
            tracker.pop()

        backtrack(0)
        return ans
        
        