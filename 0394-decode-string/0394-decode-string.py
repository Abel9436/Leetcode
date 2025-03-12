class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #solution with stack 

        stack = []  
        current_num = 0 
        current_str = '' 

        for char in s:
            if char.isdigit():
                
                current_num = current_num * 10 + int(char)
            elif char == '[':
                
                stack.append([current_num, current_str])
                current_num = 0
                current_str = ''
            elif char == ']':
                
                num, prev_str = stack.pop()
                current_str = prev_str + num * current_str
            else:
                
                current_str += char

        return current_str