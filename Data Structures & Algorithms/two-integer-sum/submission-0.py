class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sols = {}
        for i,num in enumerate(nums):
            if target-num in sols:
                return [sols[target-num],i]
            sols[num] = i
