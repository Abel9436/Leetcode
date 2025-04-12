class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            st = str(i)
            if len(st) % 2 == 0:
                print(i)
                mid = len(st) // 2
                sum1 = sum(int(n) for n in st[:mid])
                sum2 = sum(int(n) for n in st[mid::])


                if sum1 == sum2:
                    ans +=1
        return ans
