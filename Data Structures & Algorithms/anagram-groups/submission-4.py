class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = [0]*26
            for i in word:
                key[ord(i)-ord('a')] += 1
            cord = tuple(key)
            if cord not in groups:
                groups[cord] = []
            groups[cord].append(word)

        return list(groups.values())