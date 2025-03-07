class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        stack1 = []
        stack2 = []

        for str1 in s:
            if stack1 and str1 == '#':
                stack1.pop()
            else:
                if not str1 == "#":
                    stack1.append(str1)
        for str2 in t:
            if stack2 and str2 == '#':
                stack2.pop()
            else:
                if not str2 == "#":
                    stack2.append(str2)

        print(stack1,stack2)
        return stack1 == stack2




        