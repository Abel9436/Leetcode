class Solution:
    def merge(self,left_half,right_half) -> List[int]:
    # write your code here
        left, right = 0, 0
        merged = []
        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left += 1
            else:
                merged.append(right_half[right])
                right += 1
        
        while left < len(left_half):
            merged.append(left_half[left])
            left += 1
            
        while right < len(right_half):
            merged.append(right_half[right])
            right += 1
        
        return merged

    def mergeSort(self,left,right,arr):
        # write your code here
        if left == right:
            return [arr[left]]
        mid = (left + right ) // 2
    
        

        left_half = self.mergeSort(left,mid ,arr)
        right_half = self.mergeSort(mid+1,right ,arr)
        return self.merge(left_half,right_half)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(0,len(nums)-1,nums)
        