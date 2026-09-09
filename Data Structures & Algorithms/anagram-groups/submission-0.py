class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for index,val in enumerate(strs):
            sortedWord = ''.join(sorted(val))
            groups[sortedWord] = [val] + groups.get(sortedWord,[])
        res = groups.values()
        return res
