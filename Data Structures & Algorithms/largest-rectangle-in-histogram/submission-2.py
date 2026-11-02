class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        extend = heights + [0]
        for index, height in enumerate(extend):
            start = index
            while stack and stack[-1][1] > height:
                pindex,ph = stack.pop()
                area = max(area,ph * (index-pindex))
                start = pindex
            stack.append([start,height])
        return area
