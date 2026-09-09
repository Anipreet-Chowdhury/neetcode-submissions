class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count0 = nums.count(0)
        if count0 > 1:
            return [0]*len(nums)
        elif count0 == 1:
            res = [0]*len(nums)
            tot = 1
            for i in nums:
                if i != 0:
                    tot *= i
            index = nums.index(0)
            res[index] = tot
            return res
        else:
            tot = 1
            for i in nums:
                tot *= i
            res = [tot//x for x in nums]
            return res