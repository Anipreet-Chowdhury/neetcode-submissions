class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for index,val in enumerate(nums):
            remaining = target - val
            if remaining in pairs:
                return [pairs[remaining],index]
            pairs[val] = index
        

