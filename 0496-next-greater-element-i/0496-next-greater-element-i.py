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
                popped = stack.pop()
                counter[popped] = num

            
            stack.append(num)

       
        while stack:
            popped = stack.pop()
            counter[popped] = -1

        
        return [counter[num] for num in nums1]