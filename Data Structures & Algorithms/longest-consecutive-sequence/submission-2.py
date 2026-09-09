class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniq = sorted(list(set(nums)))
        mstr = 1
        strk = 1
        for index in range(0,len(uniq)-1):
            if uniq[index+1] == uniq[index]+1:
                strk += 1
            else:
                mstr = max(mstr,strk)
                strk = 1
        return max(mstr,strk)
