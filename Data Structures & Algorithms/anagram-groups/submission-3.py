from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            cord = [0]*26
            for i in word:
                cord[ord(i) - ord("a")] += 1

            key = tuple(cord)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())