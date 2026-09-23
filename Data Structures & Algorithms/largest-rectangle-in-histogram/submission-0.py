class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []
        extend = heights + [0]

        for i,h in enumerate(extend):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = height * (i-index)
                maxarea = max(maxarea, area)
                start = index

            stack.append([start,h])

        return maxarea