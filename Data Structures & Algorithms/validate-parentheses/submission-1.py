class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = set(["}","]",")"])
        pairs = {"}":"{",")":"(","]":"["}
        for i in s:
            if i in close:
                if len(stack) == 0 or pairs[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        if len(stack) != 0:
            return False
        return True