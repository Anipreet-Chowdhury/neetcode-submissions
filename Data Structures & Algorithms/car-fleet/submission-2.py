class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(list(zip(position,speed)),key=lambda x: -x[0])
        stack = []
        for p,s in pairs:
            stack.append((target-p)/s)
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)