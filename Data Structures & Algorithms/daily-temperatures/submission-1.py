class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0]*len(temperatures)
        stack = []
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pindex, ptemp = stack.pop()
                answers[pindex] = index-pindex
            stack.append([index,temp])
        return answers