class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        water = 0
        left, right = 0, len(height)-1
        mleft, mright = height[left], height[right]
        while left < right:
            if mleft < mright:
                left += 1
                mleft = max(mleft,height[left])
                water += mleft - height[left]
            else:
                right -= 1
                mright = max(mright,height[right])
                water += mright - height[right]

        return water