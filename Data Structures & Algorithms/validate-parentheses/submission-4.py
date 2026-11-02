class Solution:
    def isValid(self, s: str) -> bool:
        braks = {")":"(","}":"{","]":"["}
        stack = []
        for i in s:
            if i in braks:
                if stack == [] or braks[i] != stack.pop():
                    return False
            else:
                stack.append(i)
        if stack != []:
            return False
        return True