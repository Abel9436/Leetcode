class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] != '*':
                stack.append(s[i])
            else:
                if stack:
                    stack.pop()
        return ''.join(stack)

        