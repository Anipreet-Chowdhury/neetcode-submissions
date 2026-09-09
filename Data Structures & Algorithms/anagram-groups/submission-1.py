from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            key = "".join(sorted(word))
            res[key] = res.get(key,[]) + [word]
        return list(res.values())