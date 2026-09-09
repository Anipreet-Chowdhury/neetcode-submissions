class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dis = {}
        for index, value in enumerate(nums):
            left = target - value
            if left in dis:
                return sorted([index,dis[left]])
            dis[value] = index
