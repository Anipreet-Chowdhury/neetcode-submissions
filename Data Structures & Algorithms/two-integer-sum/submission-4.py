class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for index,num in enumerate(nums):
            val = target - num
            if val in store:
                return [store[val],index]
            store[num] = index