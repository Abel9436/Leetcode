class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        n = len(nums)
        dom, count = 0, 0

        for num, c in freq.items():
            if c > n // 2:
                dom, count = num, c
                break

        left_count = 0
        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1
            left_size = i + 1
            right_size = n - left_size
            right_count = count - left_count

            if left_count > left_size // 2 and right_count > right_size // 2:
                return i

        return -1