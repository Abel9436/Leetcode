from collections import defaultdict

class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        count = defaultdict(int)
        n = len(grid)

        # Count occurrences of each number in the grid
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        # Find the number that appears twice
        twice = [k for k, v in count.items() if v == 2]

        # Sort the keys to find the missing number
        sorted_keys = sorted(count.keys())

        # Find the missing number
        missed = None
        for i in range(1, n * n + 1):
            if i not in count:
                missed = i
                break

        return [twice[0], missed]