class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        mstr = 0
        for num in uniq:
            if num-1 not in uniq:
                strk = 1
                current = num

                while current + 1 in uniq:
                    strk += 1
                    current += 1
            
                mstr = max(mstr,strk)
        return mstr
