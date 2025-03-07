class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [0]

        for brac in s:

            if stack and brac == ")":
                popped= stack.pop()
                score = max(popped *2 ,1)
                stack[-1] +=score
            else:
                stack.append(0)
        return stack[0]

        