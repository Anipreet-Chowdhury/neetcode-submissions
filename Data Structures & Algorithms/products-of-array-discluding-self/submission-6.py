class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = nums[0], nums[-1]
        res = [1]*len(nums)
        for index in range(1,len(nums)):
            res[index] = left
            left *= nums[index]
        for index in range(len(nums)-2,-1,-1):
            res[index] *= right
            right *= nums[index]
        return res