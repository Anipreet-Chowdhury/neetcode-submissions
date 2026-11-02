class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        groups = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            l, r = index+1, len(nums)-1
            while l < r:
                val = nums[index] + nums[l] + nums[r]
                if val < 0:
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    groups.append([nums[index],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return groups