class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups = []
        for index in range(len(nums)):
            if index>0 and nums[index] == nums[index-1]:
                continue
            left , right = index+1, len(nums) -1
            while left < right:
                val = nums[left] + nums[index] + nums[right]
                if val < 0:
                    left += 1
                elif val > 0:
                    right -= 1
                else:
                    groups.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return groups