class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups = []
        for index in range(len(nums)-2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            left = index+1
            right = len(nums)-1
            while left < right:
                tot = nums[index] + nums[left] + nums[right]
                if tot < 0:
                    left += 1
                elif tot > 0:
                    right -= 1
                else:
                    groups.append([nums[index],nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return groups
