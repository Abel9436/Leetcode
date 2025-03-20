class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)

        if n < 2:
            return ''
        characters = set(s)
        print(characters)

        for i , c in enumerate(s):

            if c.swapcase() not in characters:

                left =  self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                
                if len(left) >= len(right):
                    return left
                else:
                    return right
                


            elif c.islower() and c.upper() not in characters:
                left =  self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s

        