class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            m = (l+r)//2
            t = sum([math.ceil(p/m) for p in piles])
            if t <= h:
                res = min(m,res)
                r = m-1
            else:
                l = m+1
        return res