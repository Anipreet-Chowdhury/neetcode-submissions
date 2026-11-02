class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = (s.replace(" ","")).lower()
        st = "".join([i for i in temp if (i.isalpha() or i.isdigit())])
        l, r = 0, len(st)-1
        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True