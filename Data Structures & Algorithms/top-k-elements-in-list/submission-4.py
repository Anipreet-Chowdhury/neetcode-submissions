from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        cord = {}
        for key,val in freq.items():
            cord[val] = cord.get(val,[]) + [key]
        keys = sorted(cord.keys(),reverse = True)
        res = []
        for key in keys:
            res = res + cord[key]
            if len(res) == k:
                return res
        return res