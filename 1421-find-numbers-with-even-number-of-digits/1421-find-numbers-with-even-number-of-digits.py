class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0

        # for num in nums:
        #     c = 0

        #     while num > 0:
        #         num //= 10
        #         c += 1
        #     if c % 2 == 0:
        #         counter +=1 
        # return (counter)

        for num in nums:

            if len(str(num)) % 2 == 0:
                counter +=1
        return counter