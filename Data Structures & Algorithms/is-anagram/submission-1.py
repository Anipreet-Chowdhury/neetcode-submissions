class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        wordlength = len(s)
        if len(t) != wordlength:
            return False
        counts = {}
        countt = {}
        for i in range(wordlength):
            if s[i] in counts:
                counts[s[i]] += 1
            elif s[i] not in counts:
                counts[s[i]] = 1
            if t[i] in countt:
                countt[t[i]] += 1
            elif t[i] not in countt:
                countt[t[i]] = 1
        if countt == counts:
            return True
        return False