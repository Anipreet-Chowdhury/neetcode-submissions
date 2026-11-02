class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mlen = 0
        uniq = set(nums)
        for n in uniq:
            if n-1 in uniq:
                continue
            ct = n
            sq = 1
            while ct+1 in uniq:
                sq += 1
                ct += 1
            mlen = max(mlen,sq)
        return mlen