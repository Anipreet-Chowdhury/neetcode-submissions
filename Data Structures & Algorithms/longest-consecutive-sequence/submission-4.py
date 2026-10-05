class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxsq = 0
        uniq = set(nums)
        for n in uniq:
            if n-1 in uniq:
                continue
            seq = 1
            ct = n
            while ct+1 in uniq:
                ct +=1
                seq +=1
            maxsq = max(maxsq,seq)
        return maxsq