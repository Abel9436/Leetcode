class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        chars = {
            ")":'(',
            "}":'{',
            "]":'[',

        }

        for i in range(len(s)):
            if s[i] not in chars.keys():
                stack.append(s[i])
            else:

                if not stack:
                    return False 
                popped = stack.pop()
                if popped != chars[s[i]]:
                    return False

        return stack == []

                


        