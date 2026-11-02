from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [None]*(len(nums)+1)
        counts = Counter(nums)
        for num, index in counts.items():
            if freq[index] is None:
                freq[index] = [num]
            else:
                freq[index].append(num)
        freq = [i for i in freq if i is not None]
        res = []
        for i in freq:
            res = res + i
        return res[-k:]
            