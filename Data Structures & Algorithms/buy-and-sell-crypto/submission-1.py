class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        ptr = 0
        while ptr < len(prices)-1:
            nxt = ptr + 1
            while nxt < len(prices):
                if prices[ptr] < prices[nxt]:
                    prof = max(prof,(prices[nxt]-prices[ptr]))
                nxt += 1
            ptr += 1
        return prof
                