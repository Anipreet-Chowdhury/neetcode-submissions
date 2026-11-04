class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        ptr, nxt = 0,1
        while nxt < len(prices):
            if prices[ptr] < prices[nxt]:
                prof = max(prof,(prices[nxt]-prices[ptr]))
                nxt += 1
            else:
                ptr = nxt
                nxt = ptr+1
        return prof
                