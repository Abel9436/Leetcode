class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def helper(string , i , start):
            
            if start == len(string):
                return  i == 0

            for j in range(start , len(string)):

                str_num = string[start:j+1]
                number = int(str_num)

                if number > i :
                    break

                if helper(string , i - number , j + 1):
                    return True

            return False

        ans = 0

        for k in range(1, n + 1):
            target = k * k
            if helper(str(target), k , 0):
                ans += target
        return ans

