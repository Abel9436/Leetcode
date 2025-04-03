class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = Counter(nums)

        print(freq)

        _sorted = sorted(freq.keys() , key = lambda x : freq[x], reverse = True)

        return _sorted[:k]
        