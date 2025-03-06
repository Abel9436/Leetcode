class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)

        answer = [0] * n

        for index,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                popped_index  = stack.pop()
                answer[popped_index] = index - popped_index
            stack.append(index)

        return answer

        