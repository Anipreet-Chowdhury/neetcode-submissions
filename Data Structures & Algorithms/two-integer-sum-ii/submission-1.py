class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            tot = numbers[left] + numbers[right]
            if tot < target:
                left += 1
                continue
            if tot > target:
                right -= 1
                continue
            else:
                return [left+1,right+1]