class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        counter = {}

        for num in nums2:
           
            while stack and stack[-1] < num:
                counter[stack.pop()] = num

            
            stack.append(num)

       
        while stack:
            counter[stack.pop()] = -1

        
        return [counter[num] for num in nums1]