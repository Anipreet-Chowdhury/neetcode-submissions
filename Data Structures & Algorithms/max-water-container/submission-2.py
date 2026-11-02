class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxar = 0
        l,r = 0, len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                ar = heights[l]*(r-l)
                maxar = max(maxar,ar)
                l += 1
            else:
                ar = heights[r]*(r-l)
                maxar = max(maxar,ar)
                r -= 1
        return maxar