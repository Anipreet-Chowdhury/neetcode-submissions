class Solution:
    def isValid(self, s: str) -> bool:
        braks = {"}":"{",")":"(","]":"["}
        stack = []
        for i in s:
            if i in braks:
                if len(stack) == 0:
                    return False
                elif braks[i] != stack.pop():
                    return False
            else:
                stack.append(i)

        if len(stack) > 0:
            return False
        return True