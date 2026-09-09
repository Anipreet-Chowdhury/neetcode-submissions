class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = nums.count(0)
        if count0 > 1:
            return [0]*len(nums)
        else:
            res = []
            prefix = 1
            suffix = 1
            for i in range(len(nums)):
                res.append(prefix)
                prefix = nums[i]*prefix
            for i in range(len(nums)-1,-1,-1):
                res[i] = res[i]*suffix
                suffix = suffix*nums[i]
            return res