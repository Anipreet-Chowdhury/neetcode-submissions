class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left, right = 0, len(heights) - 1
        while left < right:
            side1 = right - left 
            side2 = min(heights[left],heights[right])
            maxarea = max(maxarea, side1*side2)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxarea