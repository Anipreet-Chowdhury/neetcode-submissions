class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        els = sorted(list(zip(position,speed)), key=lambda x: [-x[0],x[1]])
        stack = []
        for p,s in els:
            stack.append((target-p)/s)
            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)