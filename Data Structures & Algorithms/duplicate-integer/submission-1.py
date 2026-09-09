class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        done = {}
        for i in nums:
            if i in done:
                return True
            done[i] = 1
        return False