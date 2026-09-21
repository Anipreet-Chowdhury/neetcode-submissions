class Solution:
    def isPalindrome(self, s: str) -> bool:
        ct = ""
        if len(s) == 1 or len(s)==0:
            return True
        for i in s:
            if i.isalpha() or i.isdigit():
                ct += i.lower()
        left = 0
        right = len(ct)-1
        while left < right:
            if ct[left] != ct[right]:
                return False
            left += 1
            right -= 1
        return True